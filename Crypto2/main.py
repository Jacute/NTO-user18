from Crypto.Util.number import long_to_bytes
import requests
import json


n = 127894990465629286464986737316516076272772707279603246243858343976808238446438470859698143217041674058139678691796966507301829438260403655283091015877351947149524219766846664436206824610443202512254657497968519627743135181026132958617790424842341201097491805100970840840901731719157058210852022379319246946551
res = ''
for i in range(135):
    flag = False
    for _ in range(10):
        req = requests.get(f'http://10.10.18.10:1177/guess_bit?bit={i}')
        pow_ = json.loads(req.text)['guess']
        if pow_ < n // 2:
            flag = True
            break
    if flag:
        res += '1'
    else:
        res += '0'
int_res = int(res, 2)
print(long_to_bytes(int_res))
