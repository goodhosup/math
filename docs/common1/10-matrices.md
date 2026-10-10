# 10. 행렬

> **먼저 알아야 할 것**: [0단계 5. 연립방정식](../basics/05-systems.md)
>
> **한 줄 요약**: 행렬은 숫자를 표처럼 묶어 놓은 것이고, 곱셈만 조금 특별합니다.

## 행렬이란?

두 가게의 과일 판매량을 표로 정리해 봅시다.

| | 사과 | 배 |
|---|---|---|
| A 가게 | 3 | 5 |
| B 가게 | 2 | 4 |

숫자만 꺼내서 괄호로 묶으면

$$
\begin{pmatrix} 3 & 5 \\ 2 & 4 \end{pmatrix}
$$

이것이 **행렬**입니다. 엑셀 표에서 숫자만 남긴 것이라고 생각하면 됩니다.

- **행**: 가로줄 (위에서부터 제1행, 제2행)
- **열**: 세로줄 (왼쪽부터 제1열, 제2열)
- **성분**: 행렬 안의 각 수. 제$i$행 제$j$열의 성분을 $a_{ij}$라고 씁니다.
- $m$개의 행, $n$개의 열로 된 행렬을 **$m \times n$ 행렬**이라고 합니다. 위 행렬은 $2 \times 2$ 행렬(이차정사각행렬)입니다.

> 💡 "행"은 가로, "열"은 세로. 헷갈리면 "**열** 맞춰!" 할 때 사람들이 앞뒤로 서는 **세로줄**을 떠올리세요.

위 예에서 $a_{12} = 5$ (A 가게의 배 판매량), $a_{21} = 2$ (B 가게의 사과 판매량)

## 같은 행렬

두 행렬이 같으려면 **크기가 같고, 같은 위치의 성분이 모두 같아야** 합니다.

$$
\begin{pmatrix} x & 2 \\ 3 & y \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 3 & 5 \end{pmatrix} \;\Rightarrow\; x = 1,\; y = 5
$$

## 덧셈, 뺄셈, 실수배: 같은 자리끼리

$$
\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} + \begin{pmatrix} 5 & 0 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 6 & 2 \\ 2 & 6 \end{pmatrix}
$$

$$
3\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = \begin{pmatrix} 3 & 6 \\ 9 & 12 \end{pmatrix}
$$

크기가 다른 행렬끼리는 더하거나 뺄 수 없습니다.

## 행렬의 곱셈: "가로 × 세로"

곱셈은 같은 자리끼리 곱하는 게 **아닙니다.** 앞 행렬의 **행(가로)**과 뒤 행렬의 **열(세로)**을 짝지어 곱해서 더합니다.

과일 예로 돌아가 봅시다. 사과 1개 1000원, 배 1개 2000원일 때 각 가게의 매출은?

$$
\begin{pmatrix} 3 & 5 \\ 2 & 4 \end{pmatrix} \begin{pmatrix} 1000 \\ 2000 \end{pmatrix}
= \begin{pmatrix} 3 \times 1000 + 5 \times 2000 \\ 2 \times 1000 + 4 \times 2000 \end{pmatrix}
= \begin{pmatrix} 13000 \\ 10000 \end{pmatrix}
$$

A 가게 매출 = (A 가게 행) · (가격 열) = $3 \times 1000 + 5 \times 2000$. 자연스럽지요?

### $2 \times 2$ 행렬끼리의 곱

$$
\begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} p & q \\ r & s \end{pmatrix}
= \begin{pmatrix} ap + br & aq + bs \\ cp + dr & cq + ds \end{pmatrix}
$$

결과의 (1행, 2열) 자리 = 앞의 **1행** $(a, b)$ × 뒤의 **2열** $(q, s)$ = $aq + bs$

**예)**

$$
\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 1 & 3 \end{pmatrix}
= \begin{pmatrix} 1 \cdot 2 + 2 \cdot 1 & 1 \cdot 0 + 2 \cdot 3 \\ 3 \cdot 2 + 4 \cdot 1 & 3 \cdot 0 + 4 \cdot 3 \end{pmatrix}
= \begin{pmatrix} 4 & 6 \\ 10 & 12 \end{pmatrix}
$$

### 곱할 수 있는 조건

$(m \times \boxed{n})$ 행렬과 $(\boxed{n} \times k)$ 행렬처럼 **앞의 열 개수 = 뒤의 행 개수**여야 곱할 수 있고, 결과는 $m \times k$ 행렬입니다.

### 주의: 순서를 바꾸면 결과가 달라질 수 있다

숫자는 $2 \times 3 = 3 \times 2$이지만, 행렬은 일반적으로

$$
AB \neq BA
$$

위 예에서 순서를 바꿔 계산해 보면 $\begin{pmatrix} 2 & 4 \\ 10 & 14 \end{pmatrix}$로 다릅니다. 그래서 $(A + B)^2 = A^2 + 2AB + B^2$도 행렬에서는 성립하지 않을 수 있어요. 올바른 전개는 $A^2 + AB + BA + B^2$입니다.

## 단위행렬 $E$

$$
E = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
$$

어떤 행렬에 곱해도 그대로입니다. 숫자의 $1$과 같은 역할이에요.

$$
AE = EA = A
$$

## 예제

**예제 1.** $A = \begin{pmatrix} 2 & -1 \\ 0 & 3 \end{pmatrix}$, $B = \begin{pmatrix} 1 & 4 \\ -2 & 1 \end{pmatrix}$일 때 $2A - B$는?

> 풀이: $\begin{pmatrix} 4 & -2 \\ 0 & 6 \end{pmatrix} - \begin{pmatrix} 1 & 4 \\ -2 & 1 \end{pmatrix} = \begin{pmatrix} 3 & -6 \\ 2 & 5 \end{pmatrix}$

**예제 2.** $\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}^2$을 계산하세요.

> 풀이: $\begin{pmatrix} 1 \cdot 1 + 2 \cdot 0 & 1 \cdot 2 + 2 \cdot 1 \\ 0 \cdot 1 + 1 \cdot 0 & 0 \cdot 2 + 1 \cdot 1 \end{pmatrix} = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}$

**예제 3.** $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 5 \\ 11 \end{pmatrix}$을 만족하는 $x$, $y$는?

> 풀이: 곱셈을 풀어 쓰면 연립방정식 $\begin{cases} x + 2y = 5 \\ 3x + 4y = 11 \end{cases}$
>
> 첫 식에 2를 곱해 빼면 $x = 1$, 그러면 $y = 2$
>
> 연립방정식을 행렬로 깔끔하게 쓸 수 있다는 것이 행렬의 큰 쓸모입니다.

## 연습문제

1. $\begin{pmatrix} 3 & 0 & -1 \\ 2 & 5 & 4 \end{pmatrix}$은 몇 행 몇 열 행렬이고, $a_{13}$, $a_{22}$는?
2. $\begin{pmatrix} 1 & 3 \\ -2 & 0 \end{pmatrix} + \begin{pmatrix} 4 & -1 \\ 2 & 2 \end{pmatrix}$
3. $\begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \end{pmatrix}$
4. $\begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix} \begin{pmatrix} 3 & 0 \\ 1 & 1 \end{pmatrix}$
5. 문제 4의 두 행렬 순서를 바꿔 곱하세요. 결과가 같나요?
6. $\begin{pmatrix} a & 1 \\ 2 & b \end{pmatrix} = \begin{pmatrix} 3 & c \\ 2 & -1 \end{pmatrix}$일 때 $a + b + c$
7. $2 \times 3$ 행렬과 $3 \times 4$ 행렬을 곱하면 어떤 크기의 행렬이 되나요?

## 정답과 풀이

1. $2 \times 3$ 행렬, $a_{13} = -1$, $a_{22} = 5$
2. $\begin{pmatrix} 5 & 2 \\ 0 & 2 \end{pmatrix}$
3. $\begin{pmatrix} 4 \\ 7 \end{pmatrix}$ ($2 + 2$, $1 + 6$)
4. $\begin{pmatrix} 4 & 1 \\ 2 & 2 \end{pmatrix}$
5. $\begin{pmatrix} 3 & 3 \\ 1 & 3 \end{pmatrix}$, 다릅니다. ($AB \neq BA$)
6. $3$ ($a = 3$, $b = -1$, $c = 1$)
7. $2 \times 4$ 행렬

---

이전 단원: [9. 경우의 수](09-counting.md) · 다음 단원: [공통수학2 - 1. 평면좌표](../common2/01-coordinates.md)

> 🎉 **공통수학1 완료!**
