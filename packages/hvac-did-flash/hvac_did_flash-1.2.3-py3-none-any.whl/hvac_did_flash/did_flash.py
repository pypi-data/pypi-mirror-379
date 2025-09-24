import subprocess
import os
import sys
import fnmatch
import shutil
import platform
import getpass
import fileinput
import re
import git
import json
import datetime
import string
import argparse
import zipfile
import tempfile
from .slack_uploader import upload_to_slack, validate_slack_config

# Constants
BUILD_SCRIPT_FILE = "build.script"
BOARD_CONFIG_FILE = "board_config.json"
DEFAULT_VECTOR_OFFSET = "04000"
ZERO_VECTOR_OFFSET = "00000"

def run_pio_command(exe_path, args, env_name=None, work_dir=None):
    """
    Run a PlatformIO command.
    
    Args:
        exe_path: Path to the PlatformIO executable
        args: List of command arguments
        env_name: Environment name for logging
        work_dir: Working directory for the command
        
    Returns:
        int: Return code of the command (0 for success)
    """
    try:
        if env_name:
            print(f"Running PlatformIO command for {env_name}: {args}")
        else:
            print(f"Running PlatformIO command: {args}")
        
        result = subprocess.run([exe_path] + args, check=True, text=True, capture_output=True, cwd=work_dir)
        print(result.stdout)
        return 0
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}")
        print(e.stderr)
        return e.returncode
    except subprocess.TimeoutExpired as e:
        print("Command timed out!")
        return e.returncode
    except Exception as e:
        print(f"An error occurred: {e}")
        return 1


def replace_serial_in_isotp_user(src_dir, did_serial_number):
    """
    src_dir/src/isotp_user.c 파일에서 '23C220001'을 did_serial_number로 대치합니다.
    """
    target_file = os.path.join(src_dir, 'src', 'isotp_user.c')
    if not os.path.exists(target_file):
        print(f"파일이 존재하지 않습니다: {target_file}")
        return
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = content.replace('23C220001', did_serial_number)
    if content != new_content:
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"isotp_user.c 내 시리얼 치환 완료: {did_serial_number}")
    else:
        print("isotp_user.c 내 치환할 문자열이 없습니다.")
        exit(1)


def replace_serial_in_bsp(src_dir, did_serial_number):
    """
    src_dir/bsp/hvac_bsp.c 파일에서 COMPILED_LOCAL_TIME 문자열을 did_serial_number로 대치합니다.
    """
    target_file = os.path.join(src_dir, 'bsp', 'hvac_bsp.c')
    if not os.path.exists(target_file):
        print(f"파일이 존재하지 않습니다: {target_file}")
        return
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = content.replace('COMPILED_LOCAL_TIME', f'"{did_serial_number}"')
    if content != new_content:
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"hvac_bsp.c 내 COMPILED_LOCAL_TIME 치환 완료: {did_serial_number}")
    else:
        print("hvac_bsp.c 내 치환할 문자열이 없습니다.")

def copy_firmware_bin_file(work_dir, did_serial_number, tag):
    """
    work_dir/.pio/build/hvac-main-stm32f103 폴더의 .bin 파일을 임시 폴더의 firmware 폴더로 복사하며,
    파일명을 hvac-main-stm32f103@{model}_{serial}_{tag}.bin 형태로 변경합니다.
    """
    src_dir = os.path.abspath(os.path.join(work_dir, '.pio', 'build', 'hvac-main-stm32f103'))
    # Use temp directory for firmware files
    temp_base_dir = tempfile.gettempdir()
    dst_dir = os.path.abspath(os.path.join(temp_base_dir, 'hvac-firmware', 'firmware'))
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    if not os.path.exists(src_dir):
        print(f"소스 폴더가 존재하지 않습니다: {src_dir}")
        return
    for file in os.listdir(src_dir):
        if file.endswith('.bin'):
            src_file = os.path.join(src_dir, file)
            # 원본 파일명에서 모델명 추출 (@ 와 _ 사이의 문자열)
            model = "AUTO"  # 기본값
            if '@' in file and '_' in file:
                start_idx = file.index('@') + 1
                end_idx = file.index('_2', start_idx) if '_2' in file[start_idx:] else len(file)
                model = file[start_idx:end_idx].replace('.bin', '')

            # 새로운 파일명 생성 (추출된 모델명 사용)
            new_filename = f"hvac-main-stm32f103@{model}_{did_serial_number}_{tag}.bin"
            dst_file = os.path.join(dst_dir, new_filename)
            shutil.copy2(src_file, dst_file)
            print(f"복사됨: {src_file} -> {dst_file}")

    print(f"Firmware files saved to temp folder: {dst_dir}")

def check_git_status(work_dir):
    """
    Check if the git repository has uncommitted changes.

    Args:
        work_dir: Working directory to check

    Returns:
        bool: True if working directory is clean, False if dirty
    """
    try:
        # Check git status
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=work_dir,
            text=True,
            capture_output=True,
            check=True
        )

        # If output is empty, working directory is clean
        if result.stdout.strip():
            return False
        return True

    except subprocess.CalledProcessError as e:
        print(f"Git status check failed: {e}")
        return False
    except FileNotFoundError:
        print("Git command not found. Please install git.")
        return False

def pio_build(env_name, did_serial_number, clean=True):
    """
    Build the project using PlatformIO.

    Args:
        env_name: Environment name
        did_serial_number: 치환할 시리얼 번호
        clean: Whether to clean before building

    Returns:
        int: Return code of the build (0 for success)
    """
    try:
        home_dir = os.path.expanduser("~")
        exe_path = f"{home_dir}\\.platformio\\penv\\Scripts\\pio.exe"

        # Check if DEV environment variable exists, otherwise use current directory
        if 'DEV' in os.environ:
            work_dir = os.path.abspath(os.path.join(os.environ['DEV'], 'upstream/hvac-main-stm32f103_pio'))
            print(f"Using DEV environment path: {work_dir}")
        else:
            # Use current working directory when DEV is not defined
            work_dir = os.getcwd()
            print(f"DEV not defined, using current directory: {work_dir}")

        # Verify the directory exists and contains platformio.ini
        platformio_ini = os.path.join(work_dir, 'platformio.ini')
        if not os.path.exists(platformio_ini):
            print(f"Error: PlatformIO project not found at: {work_dir}")
            print(f"Looking for platformio.ini at: {platformio_ini}")
            if 'DEV' in os.environ:
                print(f"Current DEV environment variable: {os.environ['DEV']}")
            else:
                print("Hint: Set DEV environment variable or run from PlatformIO project directory")
            return 1

        # Check if git working directory is clean
        if not check_git_status(work_dir):
            print("\n" + "="*60)
            print("ERROR: Git working directory is not clean!")
            print("="*60)
            print(f"The directory {work_dir} has uncommitted changes.")
            print("Please commit or stash your changes before running this program.")
            print("\nYou can check the status with: git status")
            print("To stash changes temporarily: git stash")
            print("To commit changes: git add . && git commit -m 'your message'")
            print("="*60)
            return 1
        
        # 빌드 전 git tag 정보 출력 및 체크
        try:
            tag_result = subprocess.run(["git", "describe", "--tags"], cwd=work_dir, text=True, capture_output=True, check=True)
            tag = tag_result.stdout.strip()
            print(f"현재 git 태그: {tag}")
        except subprocess.CalledProcessError:
            print("[에러] git 태그가 하나도 없습니다. 태그를 추가한 후 다시 시도하세요.")
            return 1
        
        # 빌드 전 시리얼 치환
        replace_serial_in_isotp_user(work_dir, did_serial_number)
        replace_serial_in_bsp(work_dir, did_serial_number)
        
        # Clean if requested
        if clean:
            args = ["run", "-t", "clean", "-e", env_name]
            if run_pio_command(exe_path, args, env_name, work_dir) != 0:
                return 1
        
        # Build the project
        print(f"Building {env_name}")
        args = ["run", "-e", env_name]
        if run_pio_command(exe_path, args, env_name, work_dir) != 0:
            return 1
        
        # 빌드 후 bin 파일 복사
        copy_firmware_bin_file(work_dir, did_serial_number, tag)

        # 빌드 후 git 원상복구
        restore_git_workspace(work_dir)
        
        return 0
    except Exception as e:
        print(f"Error in PIO build: {e}")
        return 1

# Serial number constants
SERIAL_FILE_NAME = "did_serial.csv"
SERIAL_KEY = "DID_SERIAL_NUMBER"
SERIAL_DATE_LENGTH = 5  # YYMDD
SERIAL_NUMBER_LENGTH = 4  # SSSS
SERIAL_TOTAL_LENGTH = SERIAL_DATE_LENGTH + SERIAL_NUMBER_LENGTH  # 9

def get_today_date_code():
    """
    Get today's date code in format YYMDD.
    
    Returns:
        str: Date code (e.g., "25F16" for Nov 16, 2025)
    """
    today = datetime.date.today()
    year = str(today.year % 100).zfill(2)  # 연도 끝 두 자리
    month_alpha = string.ascii_uppercase[today.month - 1]  # 1월=A, 6월=F
    day = str(today.day).zfill(2)
    return f"{year}{month_alpha}{day}"

def read_last_serial_from_file(filename):
    """
    Read the last serial number from file.
    
    Args:
        filename: Path to the serial file
        
    Returns:
        str or None: Last serial number or None if not found
    """
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        return None
    
    try:
        with open(filename, "r") as file:
            lines = [line.strip() for line in file if line.strip()]
            if not lines:
                return None
            
            last_line = lines[-1]
            # Extract serial number (DID_SERIAL_NUMBER=시리얼)
            if "=" in last_line:
                return last_line.split("=")[1].strip()
            else:
                return last_line.strip()
    except Exception as e:
        print(f"Error reading serial file: {e}")
        return None

def parse_serial_number(serial):
    """
    Parse a serial number into date and sequence parts.
    
    Args:
        serial: Serial number string
        
    Returns:
        tuple: (date_part, sequence_num) or (None, None) if invalid
    """
    if not serial or len(serial) < SERIAL_TOTAL_LENGTH:
        return None, None
    
    try:
        date_part = serial[:SERIAL_DATE_LENGTH]
        sequence_num = int(serial[SERIAL_DATE_LENGTH:SERIAL_DATE_LENGTH + SERIAL_NUMBER_LENGTH])
        return date_part, sequence_num
    except ValueError:
        return None, None

def create_serial_number(date_code, sequence_num):
    """
    Create a serial number from date code and sequence number.
    
    Args:
        date_code: Date code string (YYMDD)
        sequence_num: Sequence number
        
    Returns:
        str: Serial number (YYMDDSSSS)
    """
    return f"{date_code}{sequence_num:0{SERIAL_NUMBER_LENGTH}d}"

def write_serial_to_file(filename, serial):
    """
    Write serial number to file.
    
    Args:
        filename: Path to the serial file
        serial: Serial number to write
    """
    try:
        with open(filename, "w") as file:
            file.write(f"{SERIAL_KEY}={serial}\n")
    except Exception as e:
        print(f"Error writing serial file: {e}")
        raise

def get_did_serial_number():
    """
    Generate and return a unique DID serial number.
    
    The serial number format is YYMDDSSSS where:
    - YY: Year (2 digits)
    - M: Month (A-L)
    - DD: Day (2 digits)
    - SSSS: Sequence number (4 digits)
    
    Args:
        last_serial: "auto" to read from file, or a specific serial number to use as base
    
    Returns:
        str: Generated serial number
    """
    today_date_code = get_today_date_code()
    
    last_serial = read_last_serial_from_file(SERIAL_FILE_NAME)
    
    if not last_serial:
        # No previous serial, start with today's date and sequence 0001
        print(f"파일이 없거나 비어있습니다. 오늘 날짜({today_date_code}), 일련번호 0001")
        current_serial = create_serial_number(today_date_code, 1)
        next_serial = create_serial_number(today_date_code, 2)
    else:
        # Parse the last serial number
        date_part, last_sequence = parse_serial_number(last_serial)
        
        if date_part and last_sequence is not None:
            # Valid serial found, increment sequence number
            new_sequence = last_sequence + 1
            current_serial = create_serial_number(date_part, last_sequence)
            next_serial = create_serial_number(date_part, new_sequence)
            print(f"기존 날짜 유지하고 시리얼 번호만 증가: {last_serial} -> {next_serial}")
        else:
            # Invalid format, create new serial with today's date
            print(f"형식이 올바르지 않아 오늘 날짜로 새로 생성")
            current_serial = create_serial_number(today_date_code, 1)
            next_serial = create_serial_number(today_date_code, 2)
    
    # Save the next serial for future use
    write_serial_to_file(SERIAL_FILE_NAME, next_serial)
    return current_serial


def restore_git_workspace(work_dir=None):
    """
    git을 이용해 작업 폴더의 변경사항을 모두 원상복구합니다.
    추적된 파일은 마지막 커밋 상태로, 추적되지 않은 파일/폴더는 삭제합니다.
    work_dir: git 명령을 실행할 작업 디렉토리(기본값: 현재 디렉토리)
    """
    try:
        subprocess.run(["git", "reset", "--hard"], check=True, cwd=work_dir)
        subprocess.run(["git", "clean", "-fd"], check=True, cwd=work_dir)
        print(f"작업 폴더({work_dir if work_dir else os.getcwd()})가 git 기준으로 원상복구되었습니다.")
    except Exception as e:
        print(f"git 원상복구 중 오류 발생: {e}")

def compress_firmware_folder(start_serial, repeat):
    """
    임시 폴더의 firmware 폴더를 압축하여 zip 파일로 만들고, 압축 후 firmware 폴더를 삭제합니다.
    파일명은 {model}_{start_serial}_{repeat}.zip 형식입니다.
    모델명은 firmware 파일에서 추출합니다.

    Args:
        start_serial: 시작 시리얼 번호
        repeat: 반복 횟수

    Returns:
        str: 생성된 zip 파일의 경로, 실패 시 None
    """
    # Use temp directory for firmware files
    temp_base_dir = tempfile.gettempdir()
    firmware_dir = os.path.join(temp_base_dir, 'hvac-firmware', 'firmware')
    if not os.path.exists(firmware_dir):
        print(f"firmware 폴더가 존재하지 않습니다: {firmware_dir}")
        return None

    # firmware 폴더의 첫 번째 .bin 파일에서 모델명 추출
    model = "AUTO"  # 기본값
    for file in os.listdir(firmware_dir):
        if file.endswith('.bin'):
            # 파일명에서 모델명 추출 (@ 와 첫 번째 _ 사이)
            if '@' in file and '_' in file:
                start_idx = file.index('@') + 1
                end_idx = file.index('_', start_idx) if '_' in file[start_idx:] else len(file)
                model = file[start_idx:end_idx].replace('.bin', '')
                break  # 첫 번째 파일에서 모델명을 찾았으므로 중단

    # zip 파일을 저장할 hvac-firmware 폴더 생성 (temp 디렉토리에)
    output_dir = os.path.join(temp_base_dir, 'hvac-firmware')
    os.makedirs(output_dir, exist_ok=True)

    # zip 파일명 생성 (추출된 모델명 사용)
    zip_filename = f"{model}_{start_serial}_{repeat}.zip"
    zip_filepath = os.path.join(output_dir, zip_filename)

    try:
        with zipfile.ZipFile(zip_filepath, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # firmware 폴더의 모든 파일을 압축
            for root, dirs, files in os.walk(firmware_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    # firmware 폴더를 기준으로 한 상대 경로로 압축
                    arcname = os.path.relpath(file_path, os.path.dirname(firmware_dir))
                    zipf.write(file_path, arcname)

        print(f"firmware 폴더가 압축되었습니다: {zip_filepath}")

        # 임시 firmware 폴더만 삭제 (ZIP 파일은 유지)
        if os.path.exists(firmware_dir):
            shutil.rmtree(firmware_dir)
            print(f"임시 firmware 폴더가 삭제되었습니다: {firmware_dir}")
        
        return zip_filepath
        
    except Exception as e:
        print(f"압축 중 오류 발생: {e}")
        return None

def main():
    """
    Main function to process command line arguments and execute the code generation process.
    """
    # Global variables
    global home_dir
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='HVAC firmware generate tool')
    parser.add_argument('repeat', type=int, nargs='?', default=1,
                        help='Number of times to repeat the build (default: 1)')
    parser.add_argument('start_serial', type=str,
                        help='Starting serial number (e.g., 25A010001) or "auto" to read from file')
    parser.add_argument('--slack', action='store_true',
                        help='Upload generated ZIP file to Slack channel')
    
    args = parser.parse_args()
    
    # Validate repeat argument
    if args.repeat < 1:
        print(f"반복 횟수는 1 이상이어야 합니다. 입력값: {args.repeat}")
        return 1
    
    home_dir = os.path.expanduser("~")
    
    # Print system information
    system = platform.system()
    release = platform.release()
    username = getpass.getuser()
    print("Operating System:", system)
    print("OS Release:", release)
    print("User Name:", username)

    print("Model Name: AUTO (default)")
    
    # Use the provided start_serial for the first iteration
    if args.start_serial != "auto":
        write_serial_to_file(SERIAL_FILE_NAME, args.start_serial)

    start_serial = None
    for i in range(args.repeat):
        print(f"\n==== {i+1}번째 수행 ====")
        # 시리얼 번호 생성 및 출력
        serial = get_did_serial_number()
        if (start_serial is None):
            start_serial = serial
        print(f"Generated Serial Number: {serial}")
        pio_build("hvac-main-stm32f103", serial, True)
    
    # 모든 빌드가 완료된 후 firmware 폴더를 압축
    if start_serial:
        zip_file = compress_firmware_folder(start_serial, args.repeat)
        if zip_file:
            print(f"\n압축 파일 생성 완료: {zip_file}")
            
            # Slack upload if requested
            if args.slack:
                print("\n=== Slack 업로드 시작 ===")
                if validate_slack_config():
                    # Extract model name from zip filename for comment
                    zip_filename = os.path.basename(zip_file)
                    model = zip_filename.split('_')[0] if '_' in zip_filename else "AUTO"

                    # Create a descriptive comment for the upload
                    comment = f"HVAC Firmware Build - Model: {model}, Serial: {start_serial}, Count: {args.repeat}"
                    
                    if upload_to_slack(zip_file, initial_comment=comment):
                        print("Slack 업로드 성공!")
                        # Remove ZIP file after successful upload
                        try:
                            os.remove(zip_file)
                            print(f"업로드 완료 후 ZIP 파일 삭제됨: {zip_file}")
                        except Exception as e:
                            print(f"ZIP 파일 삭제 실패: {e}")
                    else:
                        print("Slack 업로드 실패. 수동으로 업로드해주세요.")
                else:
                    print("Slack 설정이 올바르지 않습니다. .env 파일을 확인해주세요.")
            else:
                print(f"이 파일을 Slack 채널에 업로드하려면 --slack 옵션을 사용하세요.")


if __name__ == "__main__":
    main()
