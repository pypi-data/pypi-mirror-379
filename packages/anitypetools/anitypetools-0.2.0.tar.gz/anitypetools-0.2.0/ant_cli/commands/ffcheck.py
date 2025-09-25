import os
from ant_cli.ffmpeg_utils import check_hls_segments_exist, check_segments_parallel
from ant_cli.storage import get_value

def execute(params):
    max_workers = 8
    try:
        max_workers = int(get_value('workers'))
    except:
        max_workers = 8
        
    print(f'Max workers: {max_workers} (ant set workers <number>)')
    
    cwd = os.getcwd()
    print(f"Current directory: {cwd}")

    file_path = os.path.join(cwd, "ant_ffcheck_errors.txt")

    # Открываем в режиме 'w' — если файл есть, он будет очищен
    with open(file_path, "w", encoding="utf-8") as f:

        m3u8_files = []
        errors_files = []

        for root, dirs, files in os.walk(cwd):
            for file in files:
                if file.endswith(".m3u8"):
                    full_path = os.path.join(root, file)
                    m3u8_files.append(full_path)

        for i in m3u8_files:
            seg_errs = []

            segs, errs1 = check_hls_segments_exist(i)

            if len(errs1) > 0:
                errs1_string = '; '.join(errs1)
                seg_errs.append(f'(MANIFEST) {i} : {errs1_string}')

            results = check_segments_parallel(i, segs, max_workers=8)  # больше потоков = быстрее

            for seg, errs2 in results.items():
                if len(errs2) > 0:
                    errs_string = '; '.join(errs2)
                    seg_errs.append(f'{seg} : {errs_string}')

            if len(seg_errs) > 0:
                errors_files.append(i)
                
                f.write(f"\n\nEPISODE {i}\n")

                for er in seg_errs:
                    f.write(f"{er}\n")
                    
        epwer = '; '.join(errors_files)
        print(f'DONE! Episodes with errors: {epwer}')