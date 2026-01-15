# 100-Prisoners-Problem

A simulation-based implementation of the 100 Prisoners Problem, comparing random guessing vs the loop-following strategy and estimating the overall success probability through repeated trials.

**Author: CWJ1222**

## 실행 방법

```bash
jupyter notebook simulation.ipynb
```

## 구현 방식

`simulation.ipynb`에서 두 가지 구현 방식을 비교합니다.

### 1. 절차적 방식 (Procedural)

| 특징 | 설명 |
|------|------|
| 인덱싱 | 0-99 |
| 전략 | 2가지 (random, optimal) |

### 2. 객체지향 방식 (OOP)

| 특징 | 설명 |
|------|------|
| 인덱싱 | 1-100 |
| 전략 | 3가지 (naive, naive_mem, optimum) |

## 시뮬레이션 결과 (100,000회 시행)

### 절차적 방식
```
 Simulation count: 100000
 Random play wins:  0.0% of simulations
Optimal play wins: 31.3% of simulations
```

### OOP 방식
```
approach       :   wins (ratio)
-----------------------------------
play_naive     :      0 (0.00%)
play_naive_mem :      0 (0.00%)
play_optimum   :  31232 (31.23%)
```

## 결론: 최적 전략

**루프 추적 전략 (play_optimal / play_optimum)**이 유일하게 효과적입니다.

| 전략 | 승률 |
|------|------|
| 무작위 선택 | ~0% |
| **루프 추적** | **~31%** |

### 루프 추적 방법
1. 자기 번호와 같은 상자를 연다
2. 그 안의 숫자가 적힌 상자를 연다
3. 자기 번호를 찾을 때까지 반복

### 왜 효과적인가?
- 상자 안 숫자들은 순환(cycle)을 형성
- 자기 번호로 시작하면 반드시 자기 번호로 돌아오는 순환에 진입
- 모든 순환 길이가 50 이하면 전원 성공 → 확률 약 31%

## 효율성 비교

| 항목 | 절차적 방식 | OOP 방식 |
|------|------------|----------|
| 코드 가독성 | 단순하고 직관적 | 모듈화되어 확장 용이 |
| 실행 속도 | 빠름 | 객체 생성 오버헤드 |
| 확장성 | 제한적 | 새 전략 추가 용이 |
