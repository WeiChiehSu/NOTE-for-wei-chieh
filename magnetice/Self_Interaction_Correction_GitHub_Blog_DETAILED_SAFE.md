# Self-interaction error and self-interaction correction (SIC)

這份筆記的核心問題是：Hartree term 把電子密度當成 classical charge density，因此會計算 density 和它自己之間的 Coulomb repulsion。對多電子系統而言，Hartree term 包含不同電子密度之間的 classical Coulomb repulsion；但是對單電子系統而言，唯一的一個電子不應該和自己產生 Coulomb repulsion。理想情況下，exchange–correlation energy 應該把這個 one-electron self-interaction 完全消掉；如果近似的 LDA、LSDA 或 GGA 做不到，就會產生 self-interaction error。

The central problem in these notes is that the Hartree term treats the electron density as a classical charge density and therefore calculates the Coulomb repulsion of the density with itself. For a many-electron system, the Hartree term contains the classical Coulomb repulsion between electron densities. However, in a one-electron system, the single electron should not repel itself. Ideally, the exchange–correlation energy should exactly cancel this one-electron self-interaction. If an approximate LDA, LSDA, or GGA functional does not cancel it exactly, a self-interaction error appears.

---

# 1. Hartree energy

Hartree term 可以寫成

The Hartree term can be written as

$$ E_H[n]=\frac{1}{2}\int d^{3}\mathbf r\int d^{3}\mathbf r'\frac{n(\mathbf r)n(\mathbf r')}{\lvert\mathbf r-\mathbf r'\rvert}. $$

這個 term 描述 electron density 之間的 classical Coulomb repulsion。

This term describes the classical Coulomb repulsion of the electron density.

前面的 factor $1/2$ 是為了避免把同一對 density contributions 重複計算兩次。

The factor $1/2$ avoids counting the same pair of density contributions twice.

---

# 2. Where the self-interaction problem comes from

問題出現在：Hartree expression 本身只看到總 density $n(\mathbf r)$。

The problem is that the Hartree expression only sees the total density $n(\mathbf r)$.

它會把 density 的所有部分都放進

It puts all parts of the density into

$$ n(\mathbf r)n(\mathbf r'). $$

因此即使只有一個電子，Hartree term 仍然會得到

Therefore, even for only one electron, the Hartree term still gives

$$ E_H[n]=\frac{1}{2}\int d^{3}\mathbf r\int d^{3}\mathbf r'\frac{n(\mathbf r)n(\mathbf r')}{\lvert\mathbf r-\mathbf r'\rvert}. $$

但是在 one-electron system 中，電子不應該和自己產生 Coulomb repulsion。

However, in a one-electron system, the electron should not produce Coulomb repulsion with itself.

所以這個 one-electron Hartree contribution 是一個 artificial self-repulsion，也就是 self-interaction。

Therefore, this one-electron Hartree contribution is an artificial self-repulsion, or self-interaction.

---

# 3. One-electron DFT total energy

對一個 one-electron system，筆記把 DFT energy 寫成

For a one-electron system, the notes write the DFT energy as

$$ E[n]=T_s[n]+\int d^{3}\mathbf r\,V(\mathbf r)n(\mathbf r)+E_H[n]+E_{xc}[n]. $$

其中

where

$$ E_H[n]=\frac{1}{2}\int d^{3}\mathbf r\int d^{3}\mathbf r'\frac{n(\mathbf r)n(\mathbf r')}{\lvert\mathbf r-\mathbf r'\rvert}. $$

對 local exchange–correlation form，可以概念性地寫成

For a local exchange–correlation form, it can be written conceptually as

$$ E_{xc}[n]=\int d^{3}\mathbf r\,n(\mathbf r)\varepsilon_{xc}(n(\mathbf r)). $$

這裡真正需要檢查的是 Hartree term 和 exchange–correlation term 的關係。

The important point here is the relation between the Hartree term and the exchange–correlation term.

---

# 4. Exact one-electron cancellation condition

對真正的 one-electron system，不存在 electron-electron repulsion。

For a true one-electron system, there is no electron-electron repulsion.

所以 Hartree self-repulsion 必須被 exchange–correlation contribution 完全消掉：

Therefore, the Hartree self-repulsion must be exactly cancelled by the exchange–correlation contribution:

$$ E_{xc}[n]+E_H[n]=0. $$

也就是

That is,

$$ E_{xc}[n]=-E_H[n]. $$

代入 Hartree expression：

Substituting the Hartree expression,

$$ E_{xc}[n]=-\frac{1}{2}\int d^{3}\mathbf r\int d^{3}\mathbf r'\frac{n(\mathbf r)n(\mathbf r')}{\lvert\mathbf r-\mathbf r'\rvert}. $$

這就是筆記中「all cancel out」的意思：對單電子系統，Hartree self-interaction 應該由 exchange–correlation term 精確抵消。

This is the meaning of “all cancel out” in the notes: for a one-electron system, the Hartree self-interaction should be cancelled exactly by the exchange–correlation term.

---

# 5. Local exchange–correlation energy per electron

如果寫成 local form

If we write

$$ E_{xc}[n]=\int d^{3}\mathbf r\,n(\mathbf r)\varepsilon_{xc}(n(\mathbf r)), $$

而又要求

and require

$$ E_{xc}[n]=-E_H[n], $$

那麼筆記想表達的圖像是：對單電子 density，exchange–correlation contribution 必須提供一個和 Hartree self-repulsion 大小相同、符號相反的 correction。

The picture in the notes is that for a one-electron density, the exchange–correlation contribution must provide a correction with the same magnitude and the opposite sign as the Hartree self-repulsion.

也就是 one-electron limit 中，不應該留下任何 residual self-repulsion。

That is, no residual self-repulsion should remain in the one-electron limit.

---

# 6. Self-interaction error in LDA and GGA

筆記指出，對近似的 LDA 或 GGA，

The notes point out that for approximate LDA or GGA functionals,

$$ E_{xc}[n]+E_H[n]\neq0. $$

也就是說，Hartree self-interaction 沒有被 exchange–correlation functional 完全消掉。

This means that the Hartree self-interaction is not completely cancelled by the exchange–correlation functional.

留下來的 residual error 就是

The residual error is

$$ \mathrm{SIE}=\text{self-interaction error}. $$

所以問題不是 Hartree term 本身「算錯」，而是 approximate exchange–correlation functional 沒有完全滿足 one-electron cancellation condition。

Therefore, the problem is not that the Hartree term itself is evaluated incorrectly. The problem is that the approximate exchange–correlation functional does not exactly satisfy the one-electron cancellation condition.

---

# 7. Physical consequence written in the notes

手寫筆記把這個 error 的物理結果寫成

The handwritten notes summarize a physical consequence as

```text
local electron
→ delocalization
```

也就是 residual self-interaction 會傾向讓電子 density 過度 delocalize。

That is, the residual self-interaction tends to make the electron density too delocalized.

這是筆記中把 SIE 和 localization / delocalization 問題連起來的地方。

This is where the notes connect the self-interaction error with localization and delocalization.

---

# 8. Basic idea of self-interaction correction

Self-interaction correction 的想法是：

The idea of self-interaction correction is:

不要只看總 density，而是把每一個 occupied orbital 自己產生的 self-interaction 分別找出來，再逐一減掉。

Instead of looking only at the total density, identify the self-interaction generated by each occupied orbital and subtract it orbital by orbital.

也就是筆記寫的：

In the language of the notes:

```text
subtract the self-interaction of every orbital, respectively
```

因此 SIC 變成 orbital-dependent correction。

Therefore, SIC becomes an orbital-dependent correction.

---

# 9. Orbital density

對第 $i$ 個 orbital 和 spin channel $\sigma$，定義 orbital density：

For orbital $i$ and spin channel $\sigma$, define the orbital density:

$$ n_{i\sigma}(\mathbf r)=\lvert\phi_{i\sigma}(\mathbf r)\rvert^{2}. $$

這個 density 只來自單一 orbital。

This density comes from only one orbital.

因此可以直接計算這個 orbital 自己的 Hartree self-energy。

Therefore, we can directly calculate the Hartree self-energy of this orbital.

---

# 10. Hartree self-energy of one orbital

筆記用 $U[n_{i\sigma}]$ 表示 orbital $i\sigma$ 自己的 Hartree energy：

The notes use $U[n_{i\sigma}]$ for the Hartree energy of orbital $i\sigma$ itself:

$$ U[n_{i\sigma}]=\frac{1}{2}\int d^{3}\mathbf r\int d^{3}\mathbf r'\frac{n_{i\sigma}(\mathbf r)n_{i\sigma}(\mathbf r')}{\lvert\mathbf r-\mathbf r'\rvert}. $$

這一項就是該 orbital 的 classical self-Coulomb contribution。

This term is the classical self-Coulomb contribution of that orbital.

---

# 11. Exchange–correlation self-energy of one orbital

對同一個 orbital density，筆記同時考慮 LSDA exchange–correlation energy：

For the same orbital density, the notes also consider the LSDA exchange–correlation energy:

$$ E_{xc}^{\mathrm{LSDA}}[n_{i\sigma},0]. $$

這裡的 notation 表示把單一 spin orbital density 放到對應的 spin channel，而另一個 spin channel 設為零。

This notation means that the density of one spin orbital is placed in its corresponding spin channel, while the other spin channel is set to zero.

所以對每一個 orbital，要去除的 self-interaction contribution 是

Therefore, for each orbital, the self-interaction contribution to be removed is

$$ U[n_{i\sigma}]+E_{xc}^{\mathrm{LSDA}}[n_{i\sigma},0]. $$

---

# 12. SIC exchange–correlation energy

筆記中的 SIC expression 可以整理成

The SIC expression in the notes can be written as

$$ E_{xc}^{\mathrm{SIC}}=E_{xc}^{\mathrm{LSDA}}[n_{\uparrow},n_{\downarrow}]-\sum_{i\sigma}\left[U[n_{i\sigma}]+E_{xc}^{\mathrm{LSDA}}[n_{i\sigma},0]\right]. $$

第一項是原本的 LSDA exchange–correlation energy：

The first term is the original LSDA exchange–correlation energy:

$$ E_{xc}^{\mathrm{LSDA}}[n_{\uparrow},n_{\downarrow}]. $$

第二項則逐 orbital 減掉

The second term subtracts, orbital by orbital,

$$ U[n_{i\sigma}]+E_{xc}^{\mathrm{LSDA}}[n_{i\sigma},0]. $$

也就是每一個 orbital 自己的 Hartree self-energy 和它自己的 LSDA exchange–correlation self-contribution。

That is, the Hartree self-energy of each orbital together with its own LSDA exchange–correlation self-contribution.

---

# 13. Corrected interaction-energy contribution

如果把 Hartree 和 exchange–correlation 兩部分放在一起，筆記中的 corrected contribution 可以寫成

If we combine the Hartree and exchange–correlation parts, the corrected contribution in the notes can be written as

$$ E_H[n]+E_{xc}^{\mathrm{LSDA}}[n_{\uparrow},n_{\downarrow}]-\sum_{i\sigma}\left[U[n_{i\sigma}]+E_{xc}^{\mathrm{LSDA}}[n_{i\sigma},0]\right]. $$

這裡最後的 summation 就是所有 orbital self-interaction contributions 的 correction。

The final summation is the correction for the self-interaction contributions of all orbitals.

---

# 14. Check the one-electron limit

SIC 最重要的檢查之一，就是 one-electron system。

One of the most important checks of SIC is the one-electron system.

如果系統只有一個 occupied orbital，總 density 就等於該 orbital density：

If there is only one occupied orbital, the total density equals that orbital density:

$$ n(\mathbf r)=n_{1\sigma}(\mathbf r). $$

因此

Therefore,

$$ E_H[n]=U[n_{1\sigma}]. $$

而 correction term 中也有

The correction term also contains

$$ U[n_{1\sigma}]+E_{xc}^{\mathrm{LSDA}}[n_{1\sigma},0]. $$

所以把 self-Hartree 和 self-exchange–correlation contribution 分別扣掉後，筆記希望保證 one-electron self-interaction 可以被精確消除。

Thus, by subtracting the self-Hartree and self-exchange–correlation contributions separately, the notes aim to ensure that the one-electron self-interaction is removed exactly.

這就是筆記中藍字寫的「ensure one-electron system self-interaction can eliminate precisely」。

This is the meaning of the handwritten note “ensure one-electron system self-interaction can eliminate precisely.”

---

# 15. Why SIC makes the Kohn–Sham equation more complicated

原本 LSDA 中，所有 orbitals 共享由總 density 決定的同一組 local potentials。

In ordinary LSDA, all orbitals share the same local potentials determined by the total density.

但是 SIC correction 依賴每一個 orbital density

However, the SIC correction depends on each orbital density

$$ n_{i\sigma}(\mathbf r)=\lvert\phi_{i\sigma}(\mathbf r)\rvert^{2}. $$

不同 orbital 一般具有不同 density：

Different orbitals generally have different densities:

$$ n_{1\sigma}(\mathbf r)\neq n_{2\sigma}(\mathbf r). $$

因此它們得到的 SIC potentials 也不同：

Therefore, they obtain different SIC potentials:

$$ V_{1\sigma}^{\mathrm{SIC}}(\mathbf r)\neq V_{2\sigma}^{\mathrm{SIC}}(\mathbf r). $$

這就是為什麼 SIC 不再是一個所有 orbitals 共用的單一 correction potential。

This is why SIC is no longer one single correction potential shared by all orbitals.

---

# 16. Orbital-dependent SIC potential

對每一個 orbital，可以形式上寫成自己的 SIC correction potential：

For each orbital, one can formally write its own SIC correction potential:

$$ V_{i\sigma}^{\mathrm{SIC}}(\mathbf r). $$

因此筆記最後把修正後的 single-particle equation 寫成

Therefore, the notes write the corrected single-particle equation as

$$ \left[\hat H^{\mathrm{LSDA}}+V_{i\sigma}^{\mathrm{SIC}}(\mathbf r)\right]\phi_{i\sigma}(\mathbf r)=\varepsilon_{i\sigma}\phi_{i\sigma}(\mathbf r). $$

和普通 LSDA 不同，這裡 potential 明確帶有 orbital index $i$。

Unlike ordinary LSDA, the potential here explicitly carries the orbital index $i$.

---

# 17. Why the orbitals must be treated separately

因為

Because

$$ V_{i\sigma}^{\mathrm{SIC}}\neq V_{j\sigma}^{\mathrm{SIC}} $$

一般成立，所以不同 orbitals 不能單純視為在完全相同的 effective potential 中運動。

in general, different orbitals cannot simply be regarded as moving in exactly the same effective potential.

筆記因此標出：

The notes therefore emphasize:

```text
correct orbital one by one
must process respectively
diagonalization becomes more complicated
```

這就是 SIC 計算比普通 LSDA 更複雜的原因。

This is why an SIC calculation is more complicated than an ordinary LSDA calculation.

---

# 18. Logic of the whole derivation

這份手寫筆記的完整邏輯是：

The complete logic of the handwritten notes is:

1. Hartree energy 是 density 和 density 之間的 classical Coulomb repulsion。
2. Hartree functional 本身也包含一個 electron density 對自己的 self-repulsion。
3. 對 one-electron system，真正物理上不應該存在 electron-electron repulsion。
4. 因此 exact one-electron limit 必須滿足 $E_{xc}[n]+E_H[n]=0$。
5. 也就是 exchange–correlation energy 必須精確 cancel Hartree self-interaction。
6. LDA、LSDA 或 GGA 一般不能做到完全 cancellation，因此留下 self-interaction error。
7. 筆記把 SIE 和 electron over-delocalization 連在一起。
8. SIC 的想法不是只修正 total density，而是逐 orbital 修正。
9. 定義 orbital density $n_{i\sigma}=\lvert\phi_{i\sigma}\rvert^{2}$。
10. 對每個 orbital 計算自己的 Hartree self-energy $U[n_{i\sigma}]$。
11. 同時取出該 orbital 自己的 LSDA exchange–correlation contribution $E_{xc}^{\mathrm{LSDA}}[n_{i\sigma},0]$。
12. 從原本 LSDA exchange–correlation energy 中逐 orbital 減去這些 self-interaction contributions。
13. 這樣設計的目的，是讓 one-electron self-interaction 可以被精確消除。
14. 但是 correction 變成 orbital-dependent。
15. 不同 orbital density 產生不同 $V_{i\sigma}^{\mathrm{SIC}}$。
16. 所以修正後的 Kohn–Sham-like equation 必須分別處理不同 orbitals，計算也因此變得更複雜。
