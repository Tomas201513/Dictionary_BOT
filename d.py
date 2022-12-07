# https://drive.google.com/file/d/1OqNUMS5zlJDIHLWNDhjuxugYtZS9_kph/view?usp=share_link

import pandas as pd
# url='https://drive.google.com/file/d/1OqNUMS5zlJDIHLWNDhjuxugYtZS9_kph/view?usp=share_link'
# url='https://drive.google.com/uc?id=' + url.split('/')[-2]
# df = pd.read_csv(url)
# print(df.head())

file_id = "1OqNUMS5zlJDIHLWNDhjuxugYtZS9_kph"  # Please set the file ID of the CSV file.

service = build('drive', 'v3', credentials=creds)
request = service.files().get_media(fileId=file_id)
fh = io.FileIO("sample.csv", mode='wb')
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
    status, done = downloader.next_chunk()
    print("Download %d%%." % int(status.progress() * 100))