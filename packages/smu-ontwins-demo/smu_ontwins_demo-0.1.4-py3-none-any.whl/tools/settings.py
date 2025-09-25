from pathlib import Path
from typing import Iterable
import pandas as pd
import numpy as np

products_index_label = ["품명", "분류", "가격"]
years_index_label = ["index","12"]

def prepare_settings(keyword: str,
                     years: list[int],
                     base_dir: str = "/content/drive/MyDrive"):
    """
    /content/drive/MyDrive/{keyword}/settings 폴더를 보장하고,
    각 연도에 대해 'co-setting-YYYY.csv'를 생성/로딩합니다.

    Returns
    -------
    (dfs, message, paths)
      - dfs: list[pd.DataFrame | None]  # years와 동일한 순서
      - message: 모든 경고/오류를 줄바꿈으로 합친 문자열(없으면 None)
      - paths: list[str]  # 파일 경로들
    """
    settings_dir = Path(base_dir) / keyword / "settings"
    settings_dir.mkdir(parents=True, exist_ok=True)

    dfs, paths, msgs = [], [], []

    def _looks_like_default_index(df: pd.DataFrame, default_index_labels: Iterable[str]) -> bool:
        """
        기대하는 인덱스 라벨(Iterable[str])과 DataFrame의 인덱스 라벨이 다르면 True.
        (라벨이 정확히 일치하면 False)
        """
        expected = [str(x) for x in default_index_labels]
        names = [("" if n is None else str(n)) for n in df.index.names]
        return names != expected

    def _prepare_product_setting():
        path = settings_dir / f"products-setting.csv"
        paths.append(str(path))

        if not path.exists():
            # 인덱스 포함 '빈 파일' 생성
            pd.DataFrame().to_csv(path, index=True, index_label=products_index_label)
            dfs.append(pd.DataFrame())
            msgs.append(f"[알림] 파일이 없어 빈 파일을 만들었습니다: {path}")

        # 파일 읽기
        try:
            df = pd.read_csv(path, index_col=0)
            warn_bits = []
            if df.empty:
                warn_bits.append("데이터가 없음")
            if _looks_like_default_index(df, products_index_label):
                warn_bits.append("잘못된 형식의 설정 파일")
            if warn_bits:
                msgs.append(f"[경고] {path} → {', '.join(warn_bits)}")
            dfs.append(df)
        except Exception as e:
            dfs.append(None)
            msgs.append(f"[오류] {path} 읽기 실패: {e}")

    def _prepare_years_setting():
        for y in years:
            path = settings_dir / f"co-setting-{int(y)}.csv"
            paths.append(str(path))

            if not path.exists():
                # 인덱스 포함 '빈 파일' 생성
                pd.DataFrame().to_csv(path, index=True, index_label=years_index_label)
                dfs.append(pd.DataFrame())
                msgs.append(f"[알림] 파일이 없어 빈 파일을 만들었습니다: {path}")
                continue

            # 파일 읽기
            try:
                df = pd.read_csv(path, index_col=0)
                warn_bits = []
                if df.empty:
                    warn_bits.append("데이터가 없음")
                if _looks_like_default_index(df, years_index_label):
                    warn_bits.append("잘못된 형식의 설정 파일")
                if warn_bits:
                    msgs.append(f"[경고] {path} → {', '.join(warn_bits)}")
                dfs.append(df)
            except Exception as e:
                dfs.append(None)
                msgs.append(f"[오류] {path} 읽기 실패: {e}")

    _prepare_product_setting()
    _prepare_years_setting()

    message = "\n".join(msgs) if msgs else None
    message = "설정값에 문제를 발견하여 더 이상 처리할 수 없습니다.\n" + message if message else None
    return dfs, message, paths
