from pathlib import Path
import pandas as pd
import numpy as np

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

    def _looks_like_default_index(df: pd.DataFrame) -> bool:
        """0..n-1의 기본 RangeIndex처럼 보이는지 점검(문자도 숫자로 변환해 검사)."""
        if df.empty:
            return False
        idx = pd.to_numeric(df.index, errors="coerce")
        return idx.notna().all() and np.array_equal(idx.to_numpy(), np.arange(len(df)))

    for y in years:
        path = settings_dir / f"co-setting-{int(y)}.csv"
        paths.append(str(path))

        if not path.exists():
            # 인덱스 포함 '빈 파일' 생성
            pd.DataFrame().to_csv(path, index=True, index_label=["index","12"])
            dfs.append(pd.DataFrame())
            msgs.append(f"[생성] 파일이 없어 빈 파일을 만들었습니다: {path}")
            continue

        # 파일 읽기
        try:
            df = pd.read_csv(path, index_col=0)
            warn_bits = []
            if df.empty:
                warn_bits.append("데이터가 없음")
            if _looks_like_default_index(df):
                warn_bits.append("인덱스가 없거나 기본 인덱스로 보임")
            if warn_bits:
                msgs.append(f"[경고] {path} → {', '.join(warn_bits)}")
            dfs.append(df)
        except Exception as e:
            dfs.append(None)
            msgs.append(f"[오류] {path} 읽기 실패: {e}")

    message = "\n".join(msgs) if msgs else None
    return dfs, message, paths
