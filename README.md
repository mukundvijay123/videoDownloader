# videoDownloader
Web app to download videos from your favorite video platforms and storing it in format (mp3 or mp4 ) of your choice.

## Table of Contents

- [Getting Started](#getting-started)
- [Installation](#installation)
- [Things to add](#things-to-add)


## Getting Started

These instructions will help you set up and run the Flask application on your local machine.

### Prerequisites

- Ensure you have Python 3.6 or higher installed on your machine. You can download Python from the [official website](https://www.python.org/downloads/).
- Ensure ffmpeg is installed on your system. [ffmpeg-download](https://www.hostinger.in/tutorials/how-to-install-ffmpeg#Installing_FFmpeg_on_CentOS_Fedora_and_RHEL)

### Installation


1. **Clone the repository**

   ```bash
   git clone https://github.com/mukundvijay123/videoDownloader.git
   cd videoDownloader
    ```

2. **Make a Virtual environment and install dependencies**

On Windows
  ```bash
  MyVenv\Scripts\activate
  ```
On Linux
   ```bash
  source MyVenv/bin/activate
  ```
Install dependencies
  ```bash
  pip install -r requirements.txt
  ```

To check if ffmpeg is installed on your sytstem.
   ```bash
   ffmpeg --version
   ```

3. **Running the app**

```bash
  cd app
  python app.py
```
The app should open in a browser tab.

## Things to add
1. Package the app into a binary using pyi-makespec.
2. Make a dynamic webpage for showing download progress and showing the URL metadata .
3. Add support for downloading playlist.



