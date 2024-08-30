from config import MailAddress, Password, SQUARE_ID
from line_client import LineClient

def main():
    client = LineClient(MailAddress, Password, device="IOSIPAD", useThrift=True)
    content = "これはCHRLINEを使用して投稿されたメッセージです。"
    
    try:
        response = client.create_post(SQUARE_ID, content)
        print(f"投稿が成功しました。投稿ID: {response['result']['feed']['postInfo']['postId']}")
    except Exception as e:
        print(f"投稿に失敗しました: {str(e)}")

if __name__ == "__main__":
    main()