class Inquiry:
    def __init__(self,
                 tXid,
                 referenceNo,
                 amt):
        self.tXid = tXid
        self.referenceNo = referenceNo
        self.amt = amt

    def jsonInquiry(self):
        return ({
            "tXid": self.tXid,
            "referenceNo": self.referenceNo,
            "amt": self.amt
        })


class BuilderInquiry:
    def __init__(self):
        self.tXid = None
        self.referenceNo = None
        self.amt = None

    def setTxid(self, tXid):
        self.tXid = tXid
        return self

    def setReferenceNo(self, referenceNo):
        self.referenceNo = referenceNo
        return self

    def setAmt(self, amt):
        self.amt = amt
        return self


class BuildInquiry(BuilderInquiry):
    def build(self):
        return Inquiry(
            self.tXid,
            self.referenceNo,
            self.amt
        )
