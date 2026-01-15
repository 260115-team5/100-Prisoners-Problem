# 100-Prisoners-Problem

A simulation-based implementation of the 100 Prisoners Problem, comparing random guessing vs the loop-following strategy and estimating the overall success probability through repeated trials.


# 100 Prisoners Problem Simulator

100 Prisoners Problem을 **몬테카를로 시뮬레이션**으로 검증하는 프로젝트입니다.

| 전략                       | 설명                                      |
| -------------------------- | ----------------------------------------- |
| **Random Strategy**        | 죄수가 서랍을 무작위로 최대 50개 열어본다 |
| **Optimal Cycle Strategy** | 사이클 추적 방식으로 서랍을 연다          |

---

## 1. Problem Summary

- 죄수 100명(1~100)이 존재
- 서랍 100개(1\~100)가 있고, 카드 1\~100이 **무작위로 1장씩** 들어있음
- 죄수는 **최대 50개**의 서랍만 열 수 있음
- 자기 번호 카드를 찾으면 성공
- **100명 전원이 성공해야** 전체가 사면

---

## 2. Strategies

### 2.1 Random Strategy

각 죄수는 100개 중 **중복 없이 50개**의 서랍을 무작위로 선택해 확인

### 2.2 Optimal Cycle Strategy

죄수 번호를 `p`라고 할 때:

1. `p`번 서랍을 연다
2. 나온 카드 번호가 `x`이면 다음에 `x`번 서랍을 연다
3. 최대 50번 반복하며 자기 번호를 찾는다

> 💡 이 전략은 "서랍 번호 → 카드 번호"를 하나의 순열로 보고 **사이클을 따라가도록** 설계되었다.

---

## 3. Expected Results

| 전략            | 전원 성공 확률       |
| --------------- | -------------------- |
| Random Strategy | ≈ 0% (사실상 불가능) |
| Cycle Strategy  | ≈ **31%**            |

---

## 4. Project Structure
```md
.
├── core/
│ ├── model.py # permutation 생성, 공통 데이터 구조
│ ├── engine.py # run_trial(), simulate()
│ └── types.py # Strategy 인터페이스
├── strategies/
│ ├── random_strategy.py
│ └── cycle_strategy.py
├── report/
│ ├── cli.py # 실행 엔트리포인트
│ └── summary.py # 결과 출력/저장
├── tests/
│ └── test_small_cases.py
├── requirements.txt
└── README.md
```

---

## 5. How to Run

### 5.1 Setup

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate    # Windows

pip install -r requirements.txt
```

### 5.2 Run Simulation

```bash
python -m report.cli --trials 20000 --seed 42
```

**옵션 예시:**

```bash
python -m report.cli --trials 50000 --seed 1 --N 100 --K 50 --out results.json
```

---

## 6. Output Example

```
Random Strategy:  wins=0/20000,    p=0.0
Cycle Strategy:   wins=6320/20000, p=0.316
```

**JSON/CSV 출력 시 포함 정보:**

- `trials`, `wins_random`, `p_random`
- `wins_cycle`, `p_cycle`
- `N`, `K`, `seed`, `timestamp`

---

## 7. Correctness Rules

> ⚠️ 시뮬레이션이 유효하려면 아래 조건을 반드시 준수해야 합니다.

- 카드 배치는 **무작위 순열** (`perm[drawer-1] = card_number`)
- Random Strategy는 **중복 없는 50개 서랍 선택**
- 각 서랍은 열고 다시 닫아야 함 (정보 공유 불가)
- 성공 판정은 **100명 전원 성공** 기준

---

## 8. Development Workflow

| 역할          | 담당 디렉토리 |
| ------------- | ------------- |
| Core/Engine   | `core/`       |
| Strategies    | `strategies/` |
| Runner/Report | `report/`     |

---

## 9. License

MIT

---

## 10. References

- [Wikipedia: 100 prisoners problem](https://en.wikipedia.org/wiki/100_prisoners_problem)
- [Rosetta Code: Python Implementation](https://rosettacode.org/wiki/100_prisoners#Python)

```

```
