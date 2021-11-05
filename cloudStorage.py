import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A7vDCs0mdwVgf3ZERBbOKV4-CVG7fQtyq7gtCtlLrBRADONlWtxs1nlQRTZOxUCAVfCVyzCWAVlqs1Cnj2FYzDxNhkMqKyBfUx_aRwPbP5E7cz3ai6YKD312Zd4n-K1Fos7xI9E'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload to dropbox: ")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File has been moved!")

main()
