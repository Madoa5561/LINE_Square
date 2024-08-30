from CHRLINE_Square import CHRLINE

class LineClient:
    def __init__(self, mailaddress: str, password: str, device: str = "IOSIPAD", useThrift: bool = True):
        self.client = CHRLINE(authTokenOrEmail=mailaddress,
                            password=password,
                            device=device,
                            useThrift=useThrift)

    def create_post(self, square_id, content):
        return self.client.createSquarePost(
            homeId=square_id,
            text=content,
            readPermissionType="ALL")
    def get_square_mid_from_ticket(self, ticket):
        return self.findSquareByInvitationTicket(ticket).square.mid