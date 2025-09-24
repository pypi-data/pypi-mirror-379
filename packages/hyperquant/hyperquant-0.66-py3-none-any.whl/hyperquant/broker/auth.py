import base64
import hmac
import urllib.parse
import time
import hashlib
from typing import Any
from aiohttp import ClientWebSocketResponse, FormData, JsonPayload
from multidict import CIMultiDict
from yarl import URL
import pybotters
import json as pyjson
from urllib.parse import urlencode


def md5_hex(s: str) -> str:
    return hashlib.md5(s.encode("utf-8")).hexdigest()



def serialize(obj, prefix=''):
    """
    Python 版 UK/v：递归排序 + urlencode + 展平
    """
    def _serialize(obj, prefix=''):
        if obj is None:
            return []
        if isinstance(obj, dict):
            items = []
            for k in sorted(obj.keys()):
                v = obj[k]
                n = f"{prefix}[{k}]" if prefix else k
                items.extend(_serialize(v, n))
            return items
        elif isinstance(obj, list):
            # JS style: output key once, then join values by &
            values = []
            for v in obj:
                if isinstance(v, dict):
                    # Recursively serialize dict, but drop key= part (just use value part)
                    sub = _serialize(v, prefix)
                    # sub is a list of key=value, but we want only value part
                    for s in sub:
                        # s is like 'key=value', need only value
                        parts = s.split('=', 1)
                        if len(parts) == 2:
                            values.append(parts[1])
                        else:
                            values.append(parts[0])
                else:
                    # Handle booleans and empty strings
                    if isinstance(v, bool):
                        val = "true" if v else "false"
                    elif v == "":
                        val = ""
                    else:
                        val = str(v)
                    values.append(val)
            return [f"{urllib.parse.quote(str(prefix))}={'&'.join(values)}"]
        else:
            # Handle booleans and empty strings
            if isinstance(obj, bool):
                val = "true" if obj else "false"
            elif obj == "":
                val = ""
            else:
                val = str(obj)
            return [f"{urllib.parse.quote(str(prefix))}={val}"]
    return "&".join(_serialize(obj, prefix))

# 🔑 Ourbit 的鉴权函数
class Auth:
    @staticmethod
    def edgex(args: tuple[str, URL], kwargs: dict[str, Any]) -> tuple[str, URL]:
        method: str = args[0]
        url: URL = args[1]
        data = kwargs.get("data") or {}
        headers: CIMultiDict = kwargs["headers"]

        session = kwargs["session"]
        api_key:str = session.__dict__["_apis"][pybotters.auth.Hosts.items[url.host].name][0]
        secret = session.__dict__["_apis"][pybotters.auth.Hosts.items[url.host].name][1]
        passphrase:str = session.__dict__["_apis"][pybotters.auth.Hosts.items[url.host].name][2]
        passphrase = passphrase.split("-")[0]
        timestamp = str(int(time.time() * 1000))
        # timestamp = "1758535055061"

        raw_body = ""
        if data and method.upper() in ["POST", "PUT", "PATCH"] and data:
            raw_body = serialize(data)
        else:
            raw_body = serialize(dict(url.query.items()))


        secret_quoted = urllib.parse.quote(secret, safe="")
        b64_secret = base64.b64encode(secret_quoted.encode("utf-8")).decode()
        message = f"{timestamp}{method.upper()}{url.raw_path}{raw_body}"
        sign = hmac.new(b64_secret.encode("utf-8"), message.encode("utf-8"), hashlib.sha256).hexdigest()
        
        sigh_header =  {
                "X-edgeX-Api-Key": api_key,
                "X-edgeX-Passphrase": passphrase,
                "X-edgeX-Signature": sign,
                "X-edgeX-Timestamp": timestamp,
        }
        # ws单独进行签名
        if headers.get("Upgrade") == "websocket":
            json_str = pyjson.dumps(sigh_header, separators=(",", ":"))
            b64_str = base64.b64encode(json_str.encode("utf-8")).decode("utf-8")
            b64_str.replace("=", "")
            headers.update({"Sec-WebSocket-Protocol": b64_str})
        else:
            headers.update(sigh_header)

        if data:
            kwargs.update({"data": JsonPayload(data)})

        return args
    
    @staticmethod
    def ourbit(args: tuple[str, URL], kwargs: dict[str, Any]) -> tuple[str, URL]:
        method: str = args[0]
        url: URL = args[1]
        data = kwargs.get("data") or {}
        headers: CIMultiDict = kwargs["headers"]

        # 从 session 里取 token
        session = kwargs["session"]
        token = session.__dict__["_apis"][pybotters.auth.Hosts.items[url.host].name][0]

        # 时间戳 & body
        now_ms = int(time.time() * 1000)
        raw_body_for_sign = (
            data
            if isinstance(data, str)
            else pyjson.dumps(data, separators=(",", ":"), ensure_ascii=False)
        )

        # 签名
        mid_hash = md5_hex(f"{token}{now_ms}")[7:]
        final_hash = md5_hex(f"{now_ms}{raw_body_for_sign}{mid_hash}")

        # 设置 headers
        headers.update(
            {
                "Authorization": token,
                "Language": "Chinese",
                "language": "Chinese",
                "Content-Type": "application/json",
                "x-ourbit-sign": final_hash,
                "x-ourbit-nonce": str(now_ms),
            }
        )

        # 更新 kwargs.body，保证发出去的与签名一致
        kwargs.update({"data": raw_body_for_sign})

        return args

    @staticmethod
    def ourbit_spot(args: tuple[str, URL], kwargs: dict[str, Any]) -> tuple[str, URL]:
        method: str = args[0]
        url: URL = args[1]
        data = kwargs.get("data") or {}
        headers: CIMultiDict = kwargs["headers"]

        # 从 session 里取 token
        session = kwargs["session"]
        token = session.__dict__["_apis"][pybotters.auth.Hosts.items[url.host].name][0]
        cookie = f"uc_token={token}; u_id={token}; "
        headers.update({"cookie": cookie})
        return args


pybotters.auth.Hosts.items["futures.ourbit.com"] = pybotters.auth.Item(
    "ourbit", Auth.ourbit
)
pybotters.auth.Hosts.items["www.ourbit.com"] = pybotters.auth.Item(
    "ourbit", Auth.ourbit_spot
)

pybotters.auth.Hosts.items["pro.edgex.exchange"] = pybotters.auth.Item(
    "edgex", Auth.edgex
)


pybotters.auth.Hosts.items["quote.edgex.exchange"] = pybotters.auth.Item(
    "edgex", Auth.edgex
)