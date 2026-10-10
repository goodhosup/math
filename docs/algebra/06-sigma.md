# 6. 수열의 합과 $\Sigma$

> **먼저 알아야 할 것**: [5. 등차수열과 등비수열](05-sequences.md)
>
> **한 줄 요약**: $\Sigma$는 "**다 더해라**"를 줄여 쓴 기호일 뿐입니다.

## $\Sigma$ 읽는 법

$$
\sum_{k=1}^{5} k^2
$$

는 "$k$에 1부터 5까지 차례로 넣어서 $k^2$을 **모두 더하라**"는 뜻입니다.

$$
\sum_{k=1}^{5} k^2 = 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 55
$$

- 아래 $k = 1$: 시작 번호
- 위 $5$: 끝 번호
- 오른쪽 $k^2$: 더할 것

> 💡 $\Sigma$(시그마)는 그리스 문자로, 영어의 S(Sum, 합)에 해당합니다. 처음에는 **항상 풀어서 써 보세요.** 그러면 무섭지 않습니다.

**예)** $\displaystyle\sum_{k=1}^{4} (2k + 1) = 3 + 5 + 7 + 9 = 24$

**예)** $\displaystyle\sum_{k=3}^{5} 2^k = 2^3 + 2^4 + 2^5 = 56$

## $\Sigma$의 성질

덧셈의 성질을 그대로 따릅니다.

$$
\sum_{k=1}^{n} (a_k \pm b_k) = \sum_{k=1}^{n} a_k \pm \sum_{k=1}^{n} b_k
$$

$$
\sum_{k=1}^{n} c\,a_k = c\sum_{k=1}^{n} a_k, \qquad \sum_{k=1}^{n} c = cn \quad (c\text{는 상수})
$$

> 💡 **주의**: 곱은 쪼갤 수 없습니다. $\displaystyle\sum a_k b_k \neq \sum a_k \times \sum b_k$

## 자연수의 거듭제곱의 합 (꼭 외울 3개)

$$
\sum_{k=1}^{n} k = \frac{n(n + 1)}{2}
$$

$$
\sum_{k=1}^{n} k^2 = \frac{n(n + 1)(2n + 1)}{6}
$$

$$
\sum_{k=1}^{n} k^3 = \left\{\frac{n(n + 1)}{2}\right\}^2
$$

> 💡 세제곱의 합은 **(그냥 합)의 제곱**이라 외우기 쉽습니다. $1^3 + 2^3 + 3^3 = 36 = 6^2 = (1 + 2 + 3)^2$

확인: $\displaystyle\sum_{k=1}^{5} k^2 = \dfrac{5 \times 6 \times 11}{6} = 55$ ✔ (위에서 직접 더한 값과 같아요)

### 활용

$$
\sum_{k=1}^{10} (2k + 3) = 2\sum_{k=1}^{10} k + \sum_{k=1}^{10} 3 = 2 \times 55 + 30 = 140
$$

## 분수 꼴의 합: 쪼개서 지우기 (부분분수)

$$
\frac{1}{k(k + 1)} = \frac{1}{k} - \frac{1}{k + 1}
$$

(확인: 오른쪽을 통분하면 $\dfrac{(k + 1) - k}{k(k + 1)}$)

이것을 이용하면

$$
\sum_{k=1}^{n} \frac{1}{k(k + 1)} = \left(1 - \frac{1}{2}\right) + \left(\frac{1}{2} - \frac{1}{3}\right) + \cdots + \left(\frac{1}{n} - \frac{1}{n + 1}\right)
$$

가운데가 연달아 지워지고 처음과 끝만 남습니다.

$$
= 1 - \frac{1}{n + 1} = \frac{n}{n + 1}
$$

## 합과 일반항의 관계

첫째 항부터 제$n$항까지의 합 $S_n$을 알면, 일반항은

$$
a_n = S_n - S_{n-1} \quad (n \ge 2), \qquad a_1 = S_1
$$

$n$번째까지의 합에서 $(n - 1)$번째까지의 합을 빼면 $n$번째 항만 남으니까요.

예) $S_n = n^2 + n$이면 $a_1 = 2$, $n \ge 2$일 때 $a_n = (n^2 + n) - \{(n - 1)^2 + (n - 1)\} = 2n$. ($n = 1$일 때도 $2$로 맞으므로 $a_n = 2n$)

## 예제

**예제 1.** $\displaystyle\sum_{k=1}^{10} (k^2 - k)$

> 풀이: $\dfrac{10 \cdot 11 \cdot 21}{6} - \dfrac{10 \cdot 11}{2} = 385 - 55 = 330$

**예제 2.** $1 \cdot 2 + 2 \cdot 3 + 3 \cdot 4 + \cdots + 10 \cdot 11$을 $\Sigma$로 쓰고 값을 구하세요.

> 풀이: $\displaystyle\sum_{k=1}^{10} k(k + 1) = \sum k^2 + \sum k = 385 + 55 = 440$

**예제 3.** $\displaystyle\sum_{k=1}^{9} \frac{1}{k(k + 1)}$

> 풀이: $\dfrac{9}{10}$

## 연습문제

1. $\displaystyle\sum_{k=1}^{4} 3k$를 풀어 쓰고 값을 구하세요.
2. $\displaystyle\sum_{k=1}^{20} k$
3. $\displaystyle\sum_{k=1}^{6} k^2$
4. $\displaystyle\sum_{k=1}^{4} k^3$
5. $\displaystyle\sum_{k=1}^{10} (3k - 2)$
6. $2 + 4 + 6 + \cdots + 40$을 $\Sigma$로 쓰고 값을 구하세요.
7. $\displaystyle\sum_{k=1}^{19} \frac{1}{k(k + 1)}$
8. $S_n = 2n^2 - n$일 때 $a_5$

## 정답과 풀이

1. $3 + 6 + 9 + 12 = 30$
2. $210$
3. $91$ ($\dfrac{6 \cdot 7 \cdot 13}{6}$)
4. $100$ ($10^2$)
5. $145$ ($3 \times 55 - 20$)
6. $\displaystyle\sum_{k=1}^{20} 2k = 2 \times 210 = 420$
7. $\dfrac{19}{20}$
8. $17$ ($S_5 - S_4 = 45 - 28$)

---

이전 단원: [5. 등차수열과 등비수열](05-sequences.md) · 다음 단원: [7. 수학적 귀납법](07-induction.md)
