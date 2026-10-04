"""碳纤维批次谱系与放行命令行冒烟入口。"""

import json
import sys
from dataclasses import asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from carbon_batch import MaterialBatch


def main() -> None:
    item = MaterialBatch(**{'batch_code': 'batch-code-001', 'product_grade': 'product-grade-001', 'process_revision': 'process-revision-001', 'status': 'draft'})
    print(json.dumps({"item": asdict(item), "fingerprint": item.fingerprint()}, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
