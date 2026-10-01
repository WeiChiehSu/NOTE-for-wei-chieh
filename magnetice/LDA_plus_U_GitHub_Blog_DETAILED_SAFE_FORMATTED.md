# DFT+U: localized orbitals, occupation matrix, double counting, and the Dudarev correction

這份筆記的主線是：普通 DFT 的能量是總電子密度 $n(\mathbf r)$ 的 functional，因此它主要看的是 total density；但是 localized $d$ 或 $f$ electrons 的物理常常取決於「哪一個 localized orbital 被佔據、佔據多少、不同 orbitals 之間是否混成」。DFT+U 因此對 selected localized subspace 加入 orbital-dependent correction。

The main idea of these notes is that ordinary DFT uses the total electron density $n(\mathbf r)$ as its basic variable. However, the physics of localized $d$ or $f$ electrons often depends on which localized orbitals are occupied, how strongly they are occupied, and whether different localized orbitals are mixed. DFT+U therefore adds an orbital-dependent correction for a selected localized subspace.

整體邏輯是：

The logical chain is:

```text
ordinary DFT
→ total density cannot directly distinguish localized orbital occupations
→ introduce a Hubbard U correction
→ subtract the interaction already counted by DFT
→ obtain E_U = U/2 sum_i n_i(1-n_i)
→ fractional occupation is penalized
→ use Janak's theorem to understand level shifts
→ project Bloch Kohn–Sham states onto localized d/f orbitals
→ build the occupation matrix
→ write the correction with Tr[n] and Tr[n^2]
→ include exchange J through U_eff = U-J
→ obtain an orbital-dependent potential
→ solve DFT+U self-consistently
```

---

# 1. Start from ordinary DFT

普通 DFT 的 total energy 可以概念性地寫成

The total energy in ordinary DFT can be written conceptually as

$$ E^{\mathrm{DFT}}[n]=T_{\mathrm{KS}}[n]+E_{\mathrm{ext}}[n]+E_H[n]+E_{xc}[n]. $$

其中 $T_{\mathrm{KS}}$ 是 non-interacting Kohn–Sham kinetic energy。

Here, $T_{\mathrm{KS}}$ is the non-interacting Kohn–Sham kinetic energy.

$E_{\mathrm{ext}}$ 是 external-potential energy。

$E_{\mathrm{ext}}$ is the external-potential energy.

$E_H$ 是 classical Coulomb energy。

$E_H$ is the classical Coulomb energy.

$E_{xc}$ 包含 exchange 和 correlation effects。

$E_{xc}$ contains exchange and correlation effects.

---

# 2. Why localized $d$ and $f$ electrons are a problem

對 localized $d$ 或 $f$ electrons，electron density 會集中在原子附近。

For localized $d$ or $f$ electrons, the electron density is concentrated around atoms.

同一個原子上的不同 $d$ 或 $f$ orbitals 彼此之間可能有很強的 local Coulomb interaction。

Different $d$ or $f$ orbitals on the same atom can have strong local Coulomb interactions.

但是 ordinary DFT 主要使用 total density

However, ordinary DFT mainly uses the total density

$$ n(\mathbf r). $$

只看 total density 時，不容易直接區分哪一個 localized orbital 被佔據，以及每一個 orbital 的 occupation 是多少。

If we only look at the total density, it is difficult to directly distinguish which localized orbital is occupied and how much each orbital is occupied.

所以 DFT+U 的想法是：

The idea of DFT+U is therefore:

```text
add an orbital-dependent correction
for selected localized d/f orbitals
```

---

# 3. A simple Hubbard-like model

先用一個簡化模型理解 $U$。

First use a simplified model to understand $U$.

假設一個原子上有很多 localized orbitals，標記為

Suppose one atom has several localized orbitals labelled by

$$ i=1,2,\ldots. $$

每一個 orbital 的 occupation 記成

The occupation of each orbital is denoted by

$$ n_i. $$

在最簡單的 integer-occupation 圖像中，

In the simplest integer-occupation picture,

$$ n_i=1 $$

代表 occupied，而

means occupied, while

$$ n_i=0 $$

代表 empty。

means empty.

---

# 4. Coulomb interaction between localized electrons

如果兩個不同 localized orbitals 都被電子佔據，它們之間會有 Coulomb interaction。

If two different localized orbitals are occupied, there is a Coulomb interaction between them.

筆記用簡化的 constant $U$ 表示每一對 localized electrons 的 interaction strength：

The notes use a simplified constant $U$ to represent the interaction strength of each pair of localized electrons:

$$ E_{ee}^{U}=\frac{1}{2}U\sum_{i\neq j}n_i n_j. $$

前面的 factor $1/2$ 是避免把 pair $(i,j)$ 和 $(j,i)$ 重複計算。

The factor $1/2$ avoids counting the pair $(i,j)$ and $(j,i)$ twice.

---

# 5. Physical meaning of the pair interaction

如果

If

$$ n_1=1,\qquad n_2=1, $$

那麼兩個 orbitals 都 occupied，所以它們之間有 interaction。

both orbitals are occupied, so they interact.

如果

If

$$ n_1=1,\qquad n_2=0, $$

那麼第二個 orbital 是 empty，所以這一對沒有 electron-electron interaction。

the second orbital is empty, so this pair has no electron-electron interaction.

所以簡化的 $n_i n_j$ 正好可以表示某一對 orbitals 是否同時有電子。

Thus, the product $n_i n_j$ indicates whether both orbitals in a pair are occupied.

---

# 6. Why the $i=j$ term is excluded

如果把 $i=j$ 也放進

If the $i=j$ term were included in

$$ \frac{1}{2}U\sum_{ij}n_i n_j, $$

就會包含

we would also include

$$ \frac{1}{2}U\sum_i n_i^{2}. $$

這代表 orbital 自己和自己產生 interaction，也就是 self-interaction-like contribution。

This represents an orbital interacting with itself, which is a self-interaction-like contribution.

因此簡化 Hubbard pair interaction 使用

Therefore, the simplified Hubbard pair interaction uses

$$ i\neq j. $$

---

# 7. Why we cannot simply add $E_{ee}^{U}$ to ordinary DFT

不能直接寫成

We cannot simply write

$$ E^{\mathrm{DFT}}+E_{ee}^{U}. $$

原因是 ordinary DFT 中的 $E_H$ 和 $E_{xc}$ 已經包含了一定程度的 electron-electron interaction。

The reason is that $E_H$ and $E_{xc}$ in ordinary DFT already contain electron-electron interaction effects.

如果再把 localized interaction $E_{ee}^{U}$ 完整加一次，就會把某一部分 interaction 計算兩次。

If the localized interaction $E_{ee}^{U}$ is added in full, part of the interaction is counted twice.

這就是 double counting。

This is the double-counting problem.

因此 DFT+U 的結構要寫成

Therefore, the DFT+U energy has the structure

$$ E^{\mathrm{DFT}+U}=E^{\mathrm{DFT}}+E_{\mathrm{interaction}}^{U}-E_{\mathrm{double\ counting}}. $$

---

# 8. Total occupation and the number of electron pairs

定義 localized shell 的總 occupation：

Define the total occupation of the localized shell:

$$ N=\sum_i n_i. $$

如果有 $N$ 個電子，總 pair number 是

For $N$ electrons, the total number of pairs is

$$ \binom{N}{2}=\frac{N(N-1)}{2}. $$

因此筆記用平均 Hubbard interaction $U$ 估計 double-counting energy：

Therefore, the notes estimate the double-counting energy using the average Hubbard interaction $U$:

$$ E_{\mathrm{double\ counting}}=\frac{1}{2}UN(N-1). $$

---

# 9. Simplified DFT+U correction

因此

Therefore,

$$ E^{\mathrm{DFT}+U}=E^{\mathrm{DFT}}+\frac{1}{2}U\sum_{i\neq j}n_i n_j-\frac{1}{2}UN(N-1). $$

把額外的 correction 定義成

Define the additional correction as

$$ E_U=\frac{1}{2}U\sum_{i\neq j}n_i n_j-\frac{1}{2}UN(N-1). $$

接下來要把這個 expression 化簡。

Next, simplify this expression.

---

# 10. Rewrite the pair sum

由

From

$$ N=\sum_i n_i, $$

得到

we obtain

$$ N^{2}=\left(\sum_i n_i\right)^{2}. $$

展開平方：

Expanding the square,

$$ N^{2}=\sum_i n_i^{2}+\sum_{i\neq j}n_i n_j. $$

所以

Therefore,

$$ \sum_{i\neq j}n_i n_j=N^{2}-\sum_i n_i^{2}. $$

把它代回 $E_U$：

Substitute this into $E_U$:

$$ E_U=\frac{1}{2}U\left(N^{2}-\sum_i n_i^{2}\right)-\frac{1}{2}U(N^{2}-N). $$

把 $N^{2}$ 消掉：

The $N^{2}$ terms cancel:

$$ E_U=\frac{1}{2}U\left(N-\sum_i n_i^{2}\right). $$

又因為

Since

$$ N=\sum_i n_i, $$

所以

we obtain

$$ E_U=\frac{U}{2}\sum_i n_i(1-n_i). $$

這就是這份筆記前半段得到的 scalar DFT+U correction。

This is the scalar DFT+U correction obtained in the first part of the notes.

---

# 11. Why fractional occupation is penalized

考慮單一 orbital 的 correction：

Consider the correction for one orbital:

$$ E_U(n_i)=\frac{U}{2}n_i(1-n_i). $$

如果

If

$$ n_i=0, $$

則

then

$$ E_U=0. $$

如果

If

$$ n_i=1, $$

則

then

$$ E_U=0. $$

但是如果

However, if

$$ n_i=\frac{1}{2}, $$

那麼

then

$$ E_U=\frac{U}{8}. $$

這是最大的 correction。

This is the maximum correction.

所以 $E_U$ 對 integer occupation $0$ 或 $1$ 不懲罰，但是會提高 fractional occupation 的能量。

Therefore, $E_U$ does not penalize integer occupations $0$ or $1$, but it raises the energy of fractional occupations.

這就是筆記中畫拋物線的原因。

This is why the handwritten notes draw a parabola.

---

# 12. Physical picture: localization versus delocalization

筆記把這個效果理解成：

The notes interpret this effect as

```text
fractional occupation
→ energy penalty
→ localized integer-like occupation is favored
```

例如兩個 localized orbitals 原本可能有

For example, two localized orbitals may initially have

$$ n_A=0.5,\qquad n_B=0.5. $$

DFT+U correction 傾向把它們推向

The DFT+U correction tends to push them toward

$$ n_A=1,\qquad n_B=0, $$

或反過來。

or the opposite configuration.

因此筆記把 $U$ 和 LDA/GGA 中 localized electrons 的 over-delocalization 問題連在一起。

Therefore, the notes connect $U$ with the over-delocalization of localized electrons in LDA/GGA.

---

# 13. Janak's theorem

筆記接著使用 Janak's theorem：

The notes next use Janak's theorem:

$$ \varepsilon_i=\frac{\partial E}{\partial n_i}. $$

它的意思是：orbital occupation $n_i$ 增加一點時，total energy 的變化率就是對應的 Kohn–Sham eigenvalue。

It means that when the orbital occupation $n_i$ changes slightly, the rate of change of the total energy is the corresponding Kohn–Sham eigenvalue.

---

# 14. Small change of an orbital occupation

把 total energy 看成 occupations 的函數：

Treat the total energy as a function of the occupations:

$$ E=E(n_1,n_2,\ldots). $$

令

Let

$$ n_i\rightarrow n_i+\delta n_i. $$

一階展開得到

To first order,

$$ \delta E\approx\frac{\partial E}{\partial n_i}\delta n_i. $$

如果

If

$$ \frac{\partial E}{\partial n_i}=\varepsilon_i, $$

那麼

then

$$ \delta E=\varepsilon_i\delta n_i. $$

所以 eigenvalue 可以理解成 occupation 改變時 total energy 的 slope。

Thus, the eigenvalue can be understood as the slope of the total energy with respect to the orbital occupation.

---

# 15. Derive Janak's relation from the Kohn–Sham energy

筆記把 Kohn–Sham energy 寫成

The notes write the Kohn–Sham energy as

$$ E[n]=T_s+\int d^{3}\mathbf r\,V_{\mathrm{ext}}(\mathbf r)n(\mathbf r)+E_H[n]+E_{xc}[n]. $$

density 寫成帶 occupation 的形式：

Write the density with orbital occupations:

$$ n(\mathbf r)=\sum_i n_i\lvert\psi_i(\mathbf r)\rvert^{2}. $$

在固定 orbitals 的 variation 中，

For a variation at fixed orbitals,

$$ \frac{\partial n(\mathbf r)}{\partial n_i}=\lvert\psi_i(\mathbf r)\rvert^{2}. $$

---

# 16. Kinetic contribution to $\partial E/\partial n_i$

Kohn–Sham kinetic energy 可以寫成

The Kohn–Sham kinetic energy can be written as

$$ T_s=\sum_i n_i\langle\psi_i\vert\hat T\vert\psi_i\rangle. $$

因此

Therefore,

$$ \frac{\partial T_s}{\partial n_i}=\langle\psi_i\vert\hat T\vert\psi_i\rangle. $$

---

# 17. External-potential contribution

external term 是

The external term is

$$ E_{\mathrm{ext}}=\int d^{3}\mathbf r\,V_{\mathrm{ext}}(\mathbf r)n(\mathbf r). $$

因此

Therefore,

$$ \frac{\partial E_{\mathrm{ext}}}{\partial n_i}=\int d^{3}\mathbf r\,V_{\mathrm{ext}}(\mathbf r)\lvert\psi_i(\mathbf r)\rvert^{2}. $$

也就是

That is,

$$ \frac{\partial E_{\mathrm{ext}}}{\partial n_i}=\langle\psi_i\vert V_{\mathrm{ext}}\vert\psi_i\rangle. $$

---

# 18. Hartree contribution

Hartree functional derivative 定義 Hartree potential：

The functional derivative of the Hartree energy defines the Hartree potential:

$$ \frac{\delta E_H[n]}{\delta n(\mathbf r)}=V_H(\mathbf r). $$

使用 chain rule：

Using the chain rule,

$$ \frac{\partial E_H}{\partial n_i}=\int d^{3}\mathbf r\,\frac{\delta E_H}{\delta n(\mathbf r)}\frac{\partial n(\mathbf r)}{\partial n_i}. $$

所以

Therefore,

$$ \frac{\partial E_H}{\partial n_i}=\int d^{3}\mathbf r\,V_H(\mathbf r)\lvert\psi_i(\mathbf r)\rvert^{2}. $$

也就是

That is,

$$ \frac{\partial E_H}{\partial n_i}=\langle\psi_i\vert V_H\vert\psi_i\rangle. $$

---

# 19. Exchange–correlation contribution

定義

Define

$$ V_{xc}(\mathbf r)=\frac{\delta E_{xc}}{\delta n(\mathbf r)}. $$

因此

Therefore,

$$ \frac{\partial E_{xc}}{\partial n_i}=\int d^{3}\mathbf r\,V_{xc}(\mathbf r)\lvert\psi_i(\mathbf r)\rvert^{2}. $$

也就是

That is,

$$ \frac{\partial E_{xc}}{\partial n_i}=\langle\psi_i\vert V_{xc}\vert\psi_i\rangle. $$

---

# 20. Combine all terms

把所有 contributions 加起來：

Adding all contributions,

$$ \frac{\partial E}{\partial n_i}=\langle\psi_i\vert\hat T+V_{\mathrm{ext}}+V_H+V_{xc}\vert\psi_i\rangle. $$

括號裡就是 Kohn–Sham Hamiltonian：

The operator in the bracket is the Kohn–Sham Hamiltonian:

$$ \hat H_{\mathrm{KS}}=\hat T+V_{\mathrm{ext}}+V_H+V_{xc}. $$

所以

Therefore,

$$ \frac{\partial E}{\partial n_i}=\langle\psi_i\vert\hat H_{\mathrm{KS}}\vert\psi_i\rangle. $$

又因為

Since

$$ \hat H_{\mathrm{KS}}\psi_i=\varepsilon_i\psi_i, $$

所以

we obtain

$$ \frac{\partial E}{\partial n_i}=\varepsilon_i. $$

這就是筆記中使用的 Janak's theorem。

This is Janak's theorem used in the notes.

---

# 21. DFT+U correction to the orbital eigenvalue

現在對

Now differentiate

$$ E_U(n_i)=\frac{U}{2}n_i(1-n_i) $$

對 $n_i$ 微分：

with respect to $n_i$:

$$ \frac{\partial E_U}{\partial n_i}=\frac{U}{2}(1-2n_i). $$

所以 DFT+U 對 orbital eigenvalue 的 shift 是

Therefore, the DFT+U shift of the orbital eigenvalue is

$$ \Delta\varepsilon_i=U\left(\frac{1}{2}-n_i\right). $$

---

# 22. Occupied, half-occupied, and empty levels

如果

If

$$ n_i=1, $$

那麼

then

$$ \Delta\varepsilon_i=-\frac{U}{2}. $$

occupied state 被往下推。

The occupied state is shifted downward.

如果

If

$$ n_i=\frac{1}{2}, $$

那麼

then

$$ \Delta\varepsilon_i=0. $$

half-occupied state 不 shift。

The half-occupied state is not shifted.

如果

If

$$ n_i=0, $$

那麼

then

$$ \Delta\varepsilon_i=+\frac{U}{2}. $$

empty state 被往上推。

The empty state is shifted upward.

所以 occupied 和 empty localized levels 之間的 separation 被拉大。

Therefore, the separation between occupied and empty localized levels increases.

---

# 23. Why we need a localized-orbital occupation matrix

到目前為止，我們把 $n_i$ 當成一個 scalar occupation。

Up to this point, we treated $n_i$ as a scalar occupation.

但在真正 solid 中，Kohn–Sham state 是 Bloch wave，而且通常不是純粹的某一個 atomic $d$ 或 $f$ orbital。

In a real solid, however, a Kohn–Sham state is a Bloch wave and is usually not a pure atomic $d$ or $f$ orbital.

例如一個 state 可能包含

For example, one state may contain

```text
Gd 4f
+ Gd 5d
+ other orbitals
```

所以要知道 localized $d/f$ occupation，必須把 Bloch Kohn–Sham states 投影到 selected localized subspace。

Therefore, to determine the localized $d/f$ occupation, the Bloch Kohn–Sham states must be projected onto a selected localized subspace.

---

# 24. Kohn–Sham density operator for one spin channel

對 spin channel $\sigma$，筆記把 density 寫成

For spin channel $\sigma$, the notes write the density as

$$ n^{\sigma}(\mathbf r)=\sum_{n\mathbf k}w_{\mathbf k}f_{n\mathbf k\sigma}\lvert\psi_{n\mathbf k\sigma}(\mathbf r)\rvert^{2}. $$

其中 $w_{\mathbf k}$ 是 k-point weight。

Here, $w_{\mathbf k}$ is the k-point weight.

$f_{n\mathbf k\sigma}$ 是 occupation。

$f_{n\mathbf k\sigma}$ is the occupation.

對應的 one-particle density operator 是

The corresponding one-particle density operator is

$$ \hat\rho^{\sigma}=\sum_{n\mathbf k}w_{\mathbf k}f_{n\mathbf k\sigma}\lvert\psi_{n\mathbf k\sigma}\rangle\langle\psi_{n\mathbf k\sigma}\rvert. $$

如果投影到 real-space position basis，

If projected onto the real-space position basis,

$$ n^{\sigma}(\mathbf r)=\langle\mathbf r\vert\hat\rho^{\sigma}\vert\mathbf r\rangle. $$

---

# 25. Define the localized Hubbard subspace

DFT+U 只特別處理 selected atom $I$ 上的 localized $d$ 或 $f$ orbitals。

DFT+U treats selected localized $d$ or $f$ orbitals on atom $I$ specially.

以 Gd $4f$ 為例，可以定義 localized basis

For Gd $4f$, for example, define localized basis functions

$$ \lvert\chi_m^{I}\rangle,\qquad m=-3,-2,\ldots,3. $$

這些 localized orbitals 張成 Hubbard subspace。

These localized orbitals span the Hubbard subspace.

---

# 26. Occupation matrix

把 density operator 投影到 localized subspace：

Project the density operator onto the localized subspace:

$$ n_{mm'}^{I\sigma}=\langle\chi_m^{I}\vert\hat\rho^{\sigma}\vert\chi_{m'}^{I}\rangle. $$

代入 density operator：

Substituting the density operator,

$$ n_{mm'}^{I\sigma}=\sum_{n\mathbf k}w_{\mathbf k}f_{n\mathbf k\sigma}\langle\chi_m^{I}\vert\psi_{n\mathbf k\sigma}\rangle\langle\psi_{n\mathbf k\sigma}\vert\chi_{m'}^{I}\rangle. $$

這就是 occupation matrix。

This is the occupation matrix.

---

# 27. Why it is a matrix instead of a scalar

如果只看 diagonal element

If we only look at a diagonal element

$$ n_{mm}^{I\sigma}, $$

它代表 spin $\sigma$ 下，localized orbital $m$ 的 occupation。

it represents the occupation of localized orbital $m$ for spin $\sigma$.

如果

If

$$ m\neq m', $$

off-diagonal element

the off-diagonal element

$$ n_{mm'}^{I\sigma} $$

描述不同 localized orbitals 之間的 mixing 或 coherence。

describes mixing or coherence between different localized orbitals.

所以真正的 localized-subspace occupation 不是單一 scalar，而是一個 matrix。

Therefore, the occupation of the localized subspace is not a single scalar but a matrix.

---

# 28. Simple two-orbital example

假設

Suppose

$$ \lvert\psi\rangle=a\lvert\chi_1\rangle+b\lvert\chi_2\rangle. $$

則 density operator 是

Then the density operator is

$$ \hat\rho=\lvert\psi\rangle\langle\psi\rvert. $$

在 $\{\chi_1,\chi_2\}$ basis 中，

In the $\{\chi_1,\chi_2\}$ basis,

$$ \mathbf n=\begin{pmatrix}\lvert a\rvert^{2}&ab^{\ast}\cr a^{\ast}b&\lvert b\rvert^{2}\end{pmatrix}. $$

diagonal elements 是 occupations。

The diagonal elements are occupations.

off-diagonal elements 代表兩個 orbitals 的 mixing。

The off-diagonal elements represent mixing between the two orbitals.

而且

Also,

$$ \left(n_{12}\right)^{\ast}=n_{21}. $$

所以 occupation matrix 是 Hermitian。

Therefore, the occupation matrix is Hermitian.

---

# 29. Diagonalize the occupation matrix

因為 $n^{I\sigma}$ 是 Hermitian matrix，所以可以 diagonalize：

Because $n^{I\sigma}$ is Hermitian, it can be diagonalized:

$$ n^{I\sigma}\lvert\alpha\rangle=\lambda_{\alpha}^{I\sigma}\lvert\alpha\rangle. $$

eigenvalues

The eigenvalues

$$ 0\leq\lambda_{\alpha}^{I\sigma}\leq1 $$

可以理解成 localized subspace 中 natural orbitals 的 occupations。

can be interpreted as occupations of the natural orbitals in the localized subspace.

---

# 30. Total occupation from the trace

localized subspace 的總 occupation 是

The total occupation of the localized subspace is

$$ N^{I\sigma}=\sum_m n_{mm}^{I\sigma}. $$

也就是

That is,

$$ N^{I\sigma}=\mathrm{Tr}\left[n^{I\sigma}\right]. $$

trace 在 basis transformation 下不變。

The trace is invariant under a basis transformation.

所以也可以寫成

Therefore,

$$ N^{I\sigma}=\sum_{\alpha}\lambda_{\alpha}^{I\sigma}. $$

---

# 31. Rewrite the scalar correction using occupation eigenvalues

原本 scalar correction 是

The original scalar correction is

$$ E_U=\frac{U}{2}\sum_i n_i(1-n_i). $$

如果用 occupation-matrix eigenvalues $\lambda_{\alpha}$ 表示，就變成

Using the eigenvalues $\lambda_{\alpha}$ of the occupation matrix,

$$ E_U=\frac{U}{2}\sum_{\alpha}\lambda_{\alpha}(1-\lambda_{\alpha}). $$

展開：

Expanding,

$$ E_U=\frac{U}{2}\left[\sum_{\alpha}\lambda_{\alpha}-\sum_{\alpha}\lambda_{\alpha}^{2}\right]. $$

利用 trace，

Using traces,

$$ \sum_{\alpha}\lambda_{\alpha}=\mathrm{Tr}[n], $$

以及

and

$$ \sum_{\alpha}\lambda_{\alpha}^{2}=\mathrm{Tr}[n^{2}]. $$

因此

Therefore,

$$ E_U=\frac{U}{2}\left[\mathrm{Tr}[n]-\mathrm{Tr}[n^{2}]\right]. $$

---

# 32. Matrix form for all atoms and spins

對所有 Hubbard atoms $I$ 和 spin channels $\sigma$ 加總：

Summing over all Hubbard atoms $I$ and spin channels $\sigma$,

$$ E_U=\frac{U}{2}\sum_{I\sigma}\left[\mathrm{Tr}[n^{I\sigma}]-\mathrm{Tr}\left[(n^{I\sigma})^{2}\right]\right]. $$

這就是從 scalar $n_i(1-n_i)$ 推廣到 occupation matrix 的方式。

This is the matrix generalization of the scalar expression $n_i(1-n_i)$.

---

# 33. Why $J$ appears

到目前為止，簡化模型只使用 direct Coulomb interaction $U$。

So far, the simplified model has used only the direct Coulomb interaction $U$.

但是同 spin electrons 還有 exchange interaction。

However, electrons with the same spin also have exchange interaction.

筆記用

The notes use

$$ U $$

表示 average direct Coulomb interaction。

for the average direct Coulomb interaction.

用

and

$$ J $$

表示 average exchange interaction。

for the average exchange interaction.

因此同 spin electrons 的 effective penalty 會接近

Therefore, the effective same-spin penalty is approximately

$$ U_{\mathrm{eff}}=U-J. $$

---

# 34. Direct Coulomb integral $U$

localized orbitals 之間的 direct Coulomb matrix element 可以概念性地寫成

The direct Coulomb matrix element between localized orbitals can be written conceptually as

$$ U_{mm'}=\int d^{3}\mathbf r\int d^{3}\mathbf r'\,\chi_m^{\ast}(\mathbf r)\chi_m(\mathbf r)\frac{e^{2}}{\lvert\mathbf r-\mathbf r'\rvert}\chi_{m'}^{\ast}(\mathbf r')\chi_{m'}(\mathbf r'). $$

它描述兩個 localized charge distributions 之間的 Coulomb repulsion。

It describes the Coulomb repulsion between two localized charge distributions.

---

# 35. Exchange integral $J$

exchange matrix element 可以概念性地寫成

The exchange matrix element can be written conceptually as

$$ J_{mm'}=\int d^{3}\mathbf r\int d^{3}\mathbf r'\,\chi_m^{\ast}(\mathbf r)\chi_{m'}(\mathbf r)\frac{e^{2}}{\lvert\mathbf r-\mathbf r'\rvert}\chi_{m'}^{\ast}(\mathbf r')\chi_m(\mathbf r'). $$

這一項來自 fermionic antisymmetry，主要影響 same-spin electrons。

This term comes from fermionic antisymmetry and mainly affects electrons with the same spin.

---

# 36. Full interaction before spherical averaging

筆記在第 5 頁先寫出更完整的 localized interaction 結構：

On page 5, the notes first write a more complete localized interaction structure:

$$ E_{\mathrm{Hub}}=\frac{1}{2}\sum_{mm'm''m'''\sigma\sigma'}\left[\langle m,m''\vert\frac{e^{2}}{\lvert\mathbf r-\mathbf r'\rvert}\vert m',m'''\rangle-\delta_{\sigma\sigma'}\langle m,m''\vert\frac{e^{2}}{\lvert\mathbf r-\mathbf r'\rvert}\vert m''',m'\rangle\right]n_{mm'}^{\sigma}n_{m''m'''}^{\sigma'}. $$

第一個 matrix element 是 direct Coulomb contribution。

The first matrix element is the direct Coulomb contribution.

第二個帶 $\delta_{\sigma\sigma'}$ 的 term 是 same-spin exchange contribution。

The second term, containing $\delta_{\sigma\sigma'}$, is the same-spin exchange contribution.

---

# 37. Dudarev simplification

做 spherical average 後，筆記把 direct interaction 用平均 $U$ 表示，把 exchange interaction 用平均 $J$ 表示。

After spherical averaging, the notes represent the direct interaction by an average $U$ and the exchange interaction by an average $J$.

最後使用

Finally, define

$$ U_{\mathrm{eff}}=U-J. $$

因此 Dudarev form 寫成

The Dudarev form becomes

$$ E_{\mathrm{corr}}=\frac{U_{\mathrm{eff}}}{2}\sum_{I\sigma}\left[\mathrm{Tr}[n^{I\sigma}]-\mathrm{Tr}\left[(n^{I\sigma})^{2}\right]\right]. $$

也可以寫成

Equivalently,

$$ E_{\mathrm{corr}}=\frac{U_{\mathrm{eff}}}{2}\sum_{I\sigma}\mathrm{Tr}\left[n^{I\sigma}(1-n^{I\sigma})\right]. $$

筆記特別標註這對應到 VASP 的 Dudarev-style implementation，例如 `LDAUTYPE=2` 的圖像。

The notes explicitly connect this to the Dudarev-style implementation used in VASP, for example the picture associated with `LDAUTYPE=2`.

---

# 38. Matrix derivative of the Dudarev energy

從

Starting from

$$ E_{\mathrm{corr}}=\frac{U_{\mathrm{eff}}}{2}\sum_{I\sigma}\left[\mathrm{Tr}[n^{I\sigma}]-\mathrm{Tr}\left[(n^{I\sigma})^{2}\right]\right], $$

對 occupation-matrix element $n_{m'm}^{I\sigma}$ 微分。

take the derivative with respect to the occupation-matrix element $n_{m'm}^{I\sigma}$.

第一項：

For the first term,

$$ \frac{\partial\mathrm{Tr}[n]}{\partial n_{m'm}}=\delta_{mm'}. $$

第二項：

For the second term,

$$ \frac{\partial\mathrm{Tr}[n^{2}]}{\partial n_{m'm}}=2n_{mm'}. $$

因此 DFT+U correction potential matrix 是

Therefore, the DFT+U correction potential matrix is

$$ V_{mm'}^{I\sigma,U}=\frac{\partial E_{\mathrm{corr}}}{\partial n_{m'm}^{I\sigma}}. $$

得到

We obtain

$$ V_{mm'}^{I\sigma,U}=U_{\mathrm{eff}}\left(\frac{1}{2}\delta_{mm'}-n_{mm'}^{I\sigma}\right). $$

---

# 39. How the $U$ potential enters the Kohn–Sham Hamiltonian

occupation matrix 是 localized-subspace quantity，所以 $V^{I\sigma,U}_{mm'}$ 也要放回 localized subspace。

The occupation matrix is defined in the localized subspace, so the potential $V^{I\sigma,U}_{mm'}$ must also act in that subspace.

對 atom $I$，可以定義 operator

For atom $I$, define the operator

$$ \hat V_U^{I\sigma}=\sum_{mm'}\lvert\chi_m^{I}\rangle V_{mm'}^{I\sigma,U}\langle\chi_{m'}^{I}\rvert. $$

把所有 Hubbard atoms 加起來：

Summing over all Hubbard atoms,

$$ \hat V_U^{\sigma}=\sum_I\hat V_U^{I\sigma}. $$

因此 Kohn–Sham equation 變成

Therefore, the Kohn–Sham equation becomes

$$ \left[\hat H_{\mathrm{DFT}}^{\sigma}+\hat V_U^{\sigma}\right]\psi_{n\mathbf k\sigma}=\varepsilon_{n\mathbf k\sigma}\psi_{n\mathbf k\sigma}. $$

---

# 40. Why occupied and empty localized levels shift in opposite directions

如果把 occupation matrix diagonalize：

If the occupation matrix is diagonalized,

$$ n^{I\sigma}\lvert\alpha\rangle=\lambda_{\alpha}\lvert\alpha\rangle, $$

那麼 $U$ potential 也在這個 basis 中變成 diagonal：

then the $U$ potential is also diagonal in this basis:

$$ V_{\alpha}^{U}=U_{\mathrm{eff}}\left(\frac{1}{2}-\lambda_{\alpha}\right). $$

如果

If

$$ \lambda_{\alpha}\approx1, $$

則

then

$$ V_{\alpha}^{U}\approx-\frac{U_{\mathrm{eff}}}{2}. $$

occupied localized level 往下 shift。

The occupied localized level shifts downward.

如果

If

$$ \lambda_{\alpha}\approx0, $$

則

then

$$ V_{\alpha}^{U}\approx+\frac{U_{\mathrm{eff}}}{2}. $$

empty localized level 往上 shift。

The empty localized level shifts upward.

因此 occupied 和 empty localized levels 的 separation 大約增加

Therefore, the separation between occupied and empty localized levels increases by approximately

$$ U_{\mathrm{eff}}. $$

---

# 41. Band shift depends on orbital character

真正的 Bloch state 通常不是 pure localized orbital。

A real Bloch state is usually not a pure localized orbital.

例如

For example,

$$ \lvert\psi\rangle=a\lvert f\rangle+b\lvert spd\rangle. $$

如果 $U$ 只作用在 $f$ subspace，那麼 energy shift 可以概念性地寫成

If $U$ acts only on the $f$ subspace, the energy shift can be viewed conceptually as

$$ \Delta\varepsilon=\langle\psi\vert\hat V_U\vert\psi\rangle. $$

如果只保留 $f$ contribution 的圖像，

If we retain only the $f$-subspace contribution in this picture,

$$ \Delta\varepsilon\sim\lvert a\rvert^{2}V_f^{U}. $$

所以 band shift 取決於這個 Bloch state 中有多少 localized orbital character。

Therefore, the band shift depends on how much localized-orbital character the Bloch state contains.

這就是筆記中「band shift is decided by how many occupations characters have」的物理意思。

This is the physical meaning of the note that the band shift depends on the occupation character of the state.

---

# 42. Why DFT+U must be self-consistent

因為 $\hat V_U$ 由 occupation matrix 決定：

Because $\hat V_U$ is determined by the occupation matrix,

$$ n_{mm'}^{I\sigma}\longrightarrow V_{mm'}^{I\sigma,U}. $$

但是 occupation matrix 又來自 Kohn–Sham wave functions：

However, the occupation matrix itself comes from the Kohn–Sham wave functions:

$$ \psi_{n\mathbf k\sigma}\longrightarrow n_{mm'}^{I\sigma}. $$

所以 DFT+U 形成新的 feedback loop：

Therefore, DFT+U introduces an additional feedback loop:

```text
Kohn–Sham wave functions
→ localized occupation matrix
→ Hubbard U potential
→ modified Kohn–Sham Hamiltonian
→ new wave functions
→ new occupation matrix
→ new Hubbard potential
→ ...
```

這就是為什麼 $U$ correction 不是 SCF 完成後再一次性加上的 post-processing energy。

This is why the $U$ correction is not a one-time post-processing energy added after the SCF calculation.

它必須進入 self-consistent Kohn–Sham cycle。

It must enter the self-consistent Kohn–Sham cycle.

---

# 43. Logic of the whole derivation

這份手寫筆記的完整邏輯是：

The complete logic of the handwritten notes is:

1. ordinary DFT 使用 total density，因此 localized orbital occupations 沒有被直接當成獨立變數。
2. localized $d/f$ electrons 在同一原子附近有強 local Coulomb interaction。
3. 用簡化的 $U$ model 寫出不同 localized orbitals 之間的 pair interaction。
4. 不能把這個 interaction 直接加到 DFT，因為 DFT 已經包含平均 electron-electron interaction，會產生 double counting。
5. 用總 occupation $N$ 和 pair number $N(N-1)/2$ 建立 double-counting subtraction。
6. 經過代數化簡得到 $E_U=U\sum_i n_i(1-n_i)/2$。
7. 這個 correction 在 $n_i=0$ 或 $1$ 時為零，在 fractional occupation 時為正，因此 penalize fractional occupation。
8. 用 Janak's theorem $\varepsilon_i=\partial E/\partial n_i$ 理解 occupation correction 如何變成 level shift。
9. 得到 $\Delta\varepsilon_i=U(1/2-n_i)$，occupied states shift down，empty states shift up。
10. 真實 solid 中 KS states 是 Bloch waves，所以不能直接把 scalar $n_i$ 當成 atomic-orbital occupation。
11. 因此把 one-particle density operator 投影到 selected localized Hubbard subspace。
12. 得到 occupation matrix $n_{mm'}^{I\sigma}$。
13. diagonal elements 是 localized orbital occupations，off-diagonal elements 描述 orbital mixing。
14. occupation matrix 是 Hermitian，可以 diagonalize 得到 natural occupations $\lambda_{\alpha}$。
15. scalar correction 可以改寫成 trace form $\mathrm{Tr}[n]-\mathrm{Tr}[n^{2}]$。
16. 真正 localized interaction還包含 same-spin exchange $J$。
17. Dudarev simplification 使用 $U_{\mathrm{eff}}=U-J$。
18. 得到 $E_{\mathrm{corr}}=U_{\mathrm{eff}}\sum_{I\sigma}\left[\mathrm{Tr}[n]-\mathrm{Tr}[n^{2}]\right]/2$。
19. 對 occupation matrix 微分得到 $V_{mm'}^{I\sigma,U}=U_{\mathrm{eff}}(\delta_{mm'}/2-n_{mm'}^{I\sigma})$。
20. 把這個 orbital-dependent potential 投影回 Hubbard subspace，加入 Kohn–Sham Hamiltonian。
21. occupied localized levels shift down，empty localized levels shift up，separation 約增加 $U_{\mathrm{eff}}$。
22. Bloch band 的實際 shift 取決於它包含多少 localized orbital character。
23. occupation matrix、$U$ potential 和 Kohn–Sham wave functions 彼此依賴，因此 DFT+U 必須 self-consistent。
