#!/usr/bin/env python3
import asyncio
import sys
import zipfile
from pathlib import Path

import httpx

# Data files to download
DOWNLOADS = [
    'http://download.geonames.org/export/dump/cities500.zip',
    'http://download.geonames.org/export/dump/cities1000.zip',
    'http://download.geonames.org/export/dump/cities5000.zip',
    'http://download.geonames.org/export/dump/cities15000.zip',
    'http://download.geonames.org/export/dump/countryInfo.txt',
    'https://www2.census.gov/geo/docs/reference/codes2020/national_county2020.txt'
]


async def download_file(client: httpx.AsyncClient, filename: str, url: str, data_dir: Path) -> bool:
    """Download a single file."""

    print(f'Downloading {filename}...')

    try:
        response = await client.get(url, follow_redirects=True)
        response.raise_for_status()
        file_path = data_dir / filename

        file_path.write_bytes(response.content)
        print(f'✓ Downloaded {filename}')
        return True

    except httpx.RequestError as e:
        print(f'✗ Network error downloading {filename}: {e}')
        return False
    except httpx.HTTPStatusError as e:
        print(f'✗ HTTP error downloading {filename}: {e.response.status_code}')
        return False
    except Exception as e:
        print(f'✗ Unexpected error downloading {filename}: {e}')
        return False


def extract_zip(zip_path: Path, extract_to: Path) -> bool:
    """Extract a zip file and remove the zip afterwards."""

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)

        zip_path.unlink()
        print(f'✓ Extracted and removed {zip_path.name}')
        return True

    except zipfile.BadZipFile:
        print(f'✗ Bad zip file: {zip_path}')
        return False
    except Exception as e:
        print(f'✗ Error extracting {zip_path}: {e}')
        return False


async def download_all_files() -> bool:
    """Download all required data files."""

    data_dir = Path('datasets')
    data_dir.mkdir(exist_ok=True)
    print(f'Downloading data to: {data_dir.absolute()}')

    success_count = 0

    # Use httpx client with reasonable timeouts
    timeout = httpx.Timeout(30, connect=10)
    async with httpx.AsyncClient(timeout=timeout, verify=False) as client:

        # Download all files concurrently
        tasks = []
        for url in DOWNLOADS:
            filename = url.split('/')[-1]

            # Keep existing files
            if data_dir.joinpath(filename.replace('.zip', '.txt')).exists():
                print(f'✓ Already exists: {filename}')
                success_count += 1
                continue

            task = download_file(client, filename, url, data_dir)
            tasks.append((task, filename))

        # Wait for all downloads to complete
        results = await asyncio.gather(*[task for task, _ in tasks], return_exceptions=True)

        # Process results and handle zip extraction
        for (_, filename), result in zip(tasks, results, strict=False):
            if isinstance(result, Exception):
                print(f'✗ Failed to download {filename}: {result}')
                continue
            elif not result:
                continue

            success_count += 1

            # Extract zip files if needed
            if filename.endswith('.zip'):
                zip_path = data_dir / filename
                if zip_path.exists():
                    extract_zip(zip_path, data_dir)

    print(f'\nCompleted: {success_count}/{len(DOWNLOADS)} files downloaded successfully')
    return success_count == len(DOWNLOADS)


def main():
    try:
        success = asyncio.run(download_all_files())
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        sys.exit('\n✗ Download interrupted by user')
    except Exception as e:
        sys.exit(f'✗ Unexpected error: {e}')


if __name__ == '__main__':
    main()
