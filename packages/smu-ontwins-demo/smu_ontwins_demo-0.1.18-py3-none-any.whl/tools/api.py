import requests
import pandas as pd
import numpy as np
from datetime import datetime

def send_to(server: str,
            events: list[dict],
            *,
            username: str = "unknown",
            bucket: str = "demo",
            measurement: str = "event",
            headers: dict | None = None,
            timeout: int = 10
            ) -> list[dict]:
    """
    dict 리스트 -> (필요시 키 매핑) -> JSON POST. 응답 요약 리스트 반환.
    """
    url = server.rstrip("/") + "/data/insert"

    handled_events = [
        {k: (pd.Timestamp(v).tz_localize('Asia/Seoul').isoformat(timespec="milliseconds")
            if isinstance(v, (pd.Timestamp, np.datetime64, datetime)) else v)
        for k, v in e.items()}
        for e in events
    ]

    s = requests.Session()
    res = []

    def _send_order(ev):
        body = {
            "bucket": bucket,
            "measurement": "customer_order_event",
            "tags": {
                "username": username,
                "team": ev.get("team", None),
                "product": ev.get("co_product", None),
            },
            "fields": {
                "quantity": ev.get("co_quantity", None)
            },
            "timestamp": ev.get("datetime", None)
        }

        r = s.post(url, json=body, headers=headers, timeout=timeout)
        try:
            payload = r.json()
        except Exception:
            payload = r.text
        res.append({"ok": r.ok, "status": r.status_code, "request": body, "response": payload})

    def _send_stock(ev):
        body = {
            "bucket": bucket,
            "measurement": "stock_status_event",
            "tags": {
                "username": username,
                "team": ev.get("team", None),
                "rack": ev.get("rack", None),
                "level": ev.get("level", None),
                "cell": ev.get("cell", None),
                "product": ev.get("product", None)
            },
            "fields": {
                "consumable": ev.get("consumable", None),
                "qty": ev.get("qty", None),
                "utilization": ev.get("utilization", None),
                "mean_ts": ev.get("mean_ts", None)
            },
            "timestamp": ev.get("datetime", None)
        }

        r = s.post(url, json=body, headers=headers, timeout=timeout)
        try:
            payload = r.json()
        except Exception:
            payload = r.text
        res.append({"ok": r.ok, "status": r.status_code, "request": body, "response": payload})

    def _send_rack_status(ev):
        body = {
            "bucket": bucket,
            "measurement": "stock_status_event",
            "tags": {
                "username": username,
                "team": ev.get("team", None),
                "rack": ev.get("rack", None),
                "level": ev.get("level", None),
                "cell": ev.get("cell", None),
                "product": ev.get("product", None)
            },
            "fields": {
                "consumable": ev.get("consumable", None),
                "qty": ev.get("qty", None),
                "utilization": ev.get("utilization", None),
                "mean_ts": ev.get("mean_ts", None)
            },
            "timestamp": ev.get("datetime", None)
        }

        r = s.post(url, json=body, headers=headers, timeout=timeout)
        try:
            payload = r.json()
        except Exception:
            payload = r.text
        res.append({"ok": r.ok, "status": r.status_code, "request": body, "response": payload})

    s = requests.Session()
    res = []

    for ev in handled_events:
        body = {
            "bucket": bucket,
            "measurement": measurement,
            "tags": {
                "team": ev.get("team", None),
                "rack": ev.get("rack", None),
                "level": ev.get("level", None),
                "cell": ev.get("cell", None)
            },
            "fields": {
                "consumable": ev.get("consumable", None),
                "product": ev.get("product", None),
                "qty": ev.get("qty", None),
                "utilization": ev.get("utilization", None),
                "mean_ts": ev.get("mean_ts", None),
                "co_product": ev.get("co_product", None),
                "co_quantity": ev.get("co_quantity", None)
            },
            "timestamp": ev.get("datetime", None)
        }

        if extra:
            body.update(extra)

        r = s.post(url, json=body, headers=headers, timeout=timeout)
        try:
            payload = r.json()
        except Exception:
            payload = r.text
        res.append({"ok": r.ok, "status": r.status_code, "request": body, "response": payload})
    return res
