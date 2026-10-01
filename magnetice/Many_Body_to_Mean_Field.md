# From the many-electron Hamiltonian to mean-field theory

這份筆記把原本的文字推導和照片上的註解合在一起。核心問題是：電子之間存在 Coulomb interaction，所以真正的 wave function 是 many-body wave function，通常不能簡單拆成單電子 wave functions 的乘積。mean-field 的想法是把兩體 electron–electron interaction 改寫成每一個電子感受到的 effective single-electron potential；Hartree term 描述平均 Coulomb field，而 fermionic antisymmetry 會再帶來 exchange。

These notes combine the original derivation with the annotations in the photo. The central problem is that the Coulomb interaction between electrons makes the true wave function a many-body wave function, so it generally cannot be separated into a simple product of single-electron wave functions. Mean-field theory replaces the two-body electron–electron interaction by an effective one-electron potential. The Hartree term describes the average Coulomb field, while fermionic antisymmetry introduces exchange.

---

# 1. Many-electron Hamiltonian

原本的 many-electron Hamiltonian 可以寫成

The many-electron Hamiltonian can be written as

$$ \widehat H_{\mathrm{electron}}=-\sum_{i=1}^{N}\frac{\nabla_{\mathbf r_i}^{2}}{2}+\sum_{i=1}^{N}\sum_{j>i}^{N}\frac{1}{r_{ij}}+\sum_{i=1}^{N}\sum_{a=1}^{K}\frac{Z_a}{r_{ia}}. $$

第一項是所有電子的 kinetic energy。

The first term is the kinetic energy of all electrons.

第二項

The second term

$$ \sum_{i=1}^{N}\sum_{j>i}^{N}\frac{1}{r_{ij}} $$

是 electron–electron Coulomb interaction。

is the electron–electron Coulomb interaction.

第三項描述電子和原子核之間的 external potential。

The third term describes the external potential from the nuclei.

> Note: 這裡先保留你原本筆記中的正號寫法。若 $Z_a$ 定義為正的核電荷，標準 atomic-unit electron–nucleus Coulomb term 通常寫成 $-Z_a/r_{ia}$。

---

# 2. The wave function is a many-body wave function

完整 Schrödinger equation 是

The full Schrödinger equation is

$$ \widehat H\Psi_i(\mathbf r_1\sigma_1,\mathbf r_2\sigma_2,\ldots,\mathbf r_N\sigma_N)=\varepsilon_i\Psi_i(\mathbf r_1\sigma_1,\mathbf r_2\sigma_2,\ldots,\mathbf r_N\sigma_N). $$

這裡的 wave function 同時依賴所有電子的位置和 spin：

The wave function depends simultaneously on the positions and spins of all electrons:

$$ \Psi_i=\Psi_i(\mathbf r_1\sigma_1,\mathbf r_2\sigma_2,\ldots,\mathbf r_N\sigma_N). $$

照片上方的註解想表達的是：真正困難的部分是

The annotation at the top of the photo emphasizes that the difficult part is

$$ \frac{1}{r_{ij}}=\frac{1}{\lvert\mathbf r_i-\mathbf r_j\rvert}. $$

因為這一項同時依賴兩個電子座標 $\mathbf r_i$ 和 $\mathbf r_j$。

This term depends on two electron coordinates, $\mathbf r_i$ and $\mathbf r_j$, at the same time.

因此不同電子的 degrees of freedom 被 coupling 在一起。

Therefore, the degrees of freedom of different electrons are coupled.

一般不能直接寫成

In general, we cannot simply write

$$ \Psi(\mathbf r_1\sigma_1,\ldots,\mathbf r_N\sigma_N)=\phi_1(\mathbf r_1\sigma_1)\phi_2(\mathbf r_2\sigma_2)\cdots\phi_N(\mathbf r_N\sigma_N). $$

也就是 many-body problem 不能直接拆成彼此獨立的 single-electron problems。

That is, the many-body problem cannot directly be separated into independent single-electron problems.

---

# 3. Why the non-interacting case can be separated

先看沒有 electron–electron interaction 的情況。

First consider the case without electron–electron interaction.

對兩個電子，

For two electrons,

$$ \widehat H=h_1(1)+h_2(2). $$

其中

where

$$ h_1(1)\phi_1(1)=\varepsilon_1\phi_1(1), $$

以及

and

$$ h_2(2)\phi_2(2)=\varepsilon_2\phi_2(2). $$

假設 total wave function 是單電子 wave functions 的 product：

Assume the total wave function is a product of single-electron wave functions:

$$ \psi(1,2)=\phi_1(1)\phi_2(2). $$

讓 Hamiltonian 作用：

Apply the Hamiltonian:

$$ \widehat H\psi=[h_1(1)+h_2(2)][\phi_1(1)\phi_2(2)]. $$

因為 $h_1$ 只作用在 electron 1，

Because $h_1$ acts only on electron 1,

$$ h_1(1)[\phi_1(1)\phi_2(2)]=[h_1(1)\phi_1(1)]\phi_2(2). $$

同樣地，

Similarly,

$$ h_2(2)[\phi_1(1)\phi_2(2)]=\phi_1(1)[h_2(2)\phi_2(2)]. $$

所以

Therefore,

$$ \widehat H\psi=\varepsilon_1\phi_1(1)\phi_2(2)+\varepsilon_2\phi_1(1)\phi_2(2). $$

整理後

After simplification,

$$ \widehat H\psi=(\varepsilon_1+\varepsilon_2)\phi_1(1)\phi_2(2). $$

因此在沒有 electron–electron interaction 時，wave function 可以 separation。

Therefore, without electron–electron interaction, the wave function can be separated.

---

# 4. Why electron–electron interaction destroys simple separability

現在加入 electron–electron interaction：

Now include electron–electron interaction:

$$ \widehat H=h_1(1)+h_2(2)+\frac{1}{\lvert\mathbf r_1-\mathbf r_2\rvert}. $$

如果仍然先嘗試 product state

If we still try the product state

$$ \psi(1,2)=\phi_1(1)\phi_2(2), $$

那麼

then

$$ \widehat H\psi=\left[h_1(1)+h_2(2)+\frac{1}{\lvert\mathbf r_1-\mathbf r_2\rvert}\right]\phi_1(1)\phi_2(2). $$

前兩項仍然可以分開：

The first two terms remain separable:

$$ h_1(1)\phi_1(1)\phi_2(2)=\varepsilon_1\phi_1(1)\phi_2(2), $$

$$ h_2(2)\phi_1(1)\phi_2(2)=\varepsilon_2\phi_1(1)\phi_2(2). $$

但是 interaction term 變成

However, the interaction term becomes

$$ \frac{1}{\lvert\mathbf r_1-\mathbf r_2\rvert}\phi_1(1)\phi_2(2). $$

其中 $\mathbf r_1$ 和 $\mathbf r_2$ 同時出現在同一個 factor 中。

The coordinates $\mathbf r_1$ and $\mathbf r_2$ appear together in the same factor.

因此它不能被拆成「只依賴 electron 1」和「只依賴 electron 2」的兩個獨立 terms。

Therefore, it cannot be decomposed into one term depending only on electron 1 and another term depending only on electron 2.

所以

Thus,

$$ \widehat H\psi=\varepsilon_1\phi_1(1)\phi_2(2)+\varepsilon_2\phi_1(1)\phi_2(2)+\frac{1}{\lvert\mathbf r_1-\mathbf r_2\rvert}\phi_1(1)\phi_2(2), $$

而這個問題一般不能再化成兩個完全獨立的 single-electron equations。

and in general this cannot be reduced to two completely independent single-electron equations.

這就是照片上方紅字在強調的「兩體作用把不同電子座標 coupling 在一起」。

This is the point emphasized by the red annotation at the top of the photo: the two-body interaction couples different electron coordinates.

---

# 5. Mean-field idea

照片中間的黑字把 mean-field 的物理圖像寫得很直接：

The black annotation in the middle of the photo gives the physical picture of mean-field theory:

```text
electron–electron interaction
→ each electron moves in an average field generated by the other electrons
→ mean field
```

原本真正的 two-body interaction 是

The original two-body interaction is

$$ \frac{1}{\lvert\mathbf r_i-\mathbf r_j\rvert}. $$

mean-field approximation 的想法是把它改成 single-electron effective potential：

The idea of the mean-field approximation is to replace it by an effective single-electron potential:

$$ \frac{1}{\lvert\mathbf r_i-\mathbf r_j\rvert}\longrightarrow V_{ee}(\mathbf r_i). $$

照片上的藍字可以整理成：

The blue annotation in the photo can be summarized as:

```text
two-body interaction
→ effective one-electron potential
```

這就是從 many-body problem 往 effective single-electron problem 前進的關鍵。

This is the key step from the many-body problem toward an effective single-electron problem.

---

# 6. Hartree mean field

最直接的 mean-field Coulomb potential 是 Hartree potential：

The simplest mean-field Coulomb potential is the Hartree potential:

$$ V_H(\mathbf r)=\int d^{3}\mathbf r'\frac{n(\mathbf r')}{\lvert\mathbf r-\mathbf r'\rvert}. $$

這裡 $n(\mathbf r')$ 是其他電子形成的平均 electron density。

Here, $n(\mathbf r')$ is the average electron density generated by the electrons.

對位置 $\mathbf r$ 的電子而言，它不再逐一追蹤「electron 2 現在在哪裡、electron 3 現在在哪裡」。

For an electron at position $\mathbf r$, we no longer track the instantaneous position of electron 2, electron 3, and so on one by one.

而是感受到由整體 electron density 產生的平均 Coulomb field。

Instead, it feels the average Coulomb field generated by the total electron density.

因此

Therefore,

$$ \frac{1}{\lvert\mathbf r-\mathbf r'\rvert}\longrightarrow V_H(\mathbf r). $$

這就是照片中藍字標出的 Hartree term。

This is the Hartree term highlighted in blue in the photo.

---

# 7. Why Hartree alone is not enough

如果電子只是 classical distinguishable particles，平均 Coulomb field 可能已經捕捉了主要 interaction。

If electrons were classical distinguishable particles, the average Coulomb field would capture the main interaction.

但是電子是 fermions。

However, electrons are fermions.

所以 many-electron wave function 還必須滿足 antisymmetry：

Therefore, the many-electron wave function must also satisfy antisymmetry:

$$ \Psi(\ldots,x_i,\ldots,x_j,\ldots)=-\Psi(\ldots,x_j,\ldots,x_i,\ldots). $$

其中

where

$$ x_i=(\mathbf r_i,\sigma_i). $$

這就是照片下半部藍字「電子是費米子，還需要反對稱」的內容。

This is the meaning of the blue annotation in the lower half of the photo: electrons are fermions, so antisymmetry is also required.

---

# 8. Two-electron antisymmetric wave function

對兩個 electrons，如果 single-particle orbitals 是 $\phi_1$ 和 $\phi_2$，antisymmetric combination 可以寫成

For two electrons with single-particle orbitals $\phi_1$ and $\phi_2$, an antisymmetric combination can be written as

$$ \Psi(1,2)=\frac{1}{\sqrt{2}}\left[\phi_1(1)\phi_2(2)-\phi_2(1)\phi_1(2)\right]. $$

交換 electron 1 和 electron 2：

Exchange electron 1 and electron 2:

$$ \Psi(2,1)=\frac{1}{\sqrt{2}}\left[\phi_1(2)\phi_2(1)-\phi_2(2)\phi_1(1)\right]. $$

整理後

After rearranging,

$$ \Psi(2,1)=-\Psi(1,2). $$

所以 minus sign 正是 fermionic exchange antisymmetry。

Therefore, the minus sign is the fermionic exchange antisymmetry.

---

# 9. Slater determinant

對兩個 electrons，上面的 antisymmetric wave function 可以寫成 Slater determinant：

For two electrons, the antisymmetric wave function can be written as a Slater determinant:

$$ \Psi(1,2)=\frac{1}{\sqrt{2}}\mathrm{det}\begin{pmatrix}\phi_1(1)&\phi_1(2)\cr\phi_2(1)&\phi_2(2)\end{pmatrix}. $$

展開 determinant：

Expanding the determinant,

$$ \Psi(1,2)=\frac{1}{\sqrt{2}}\left[\phi_1(1)\phi_2(2)-\phi_2(1)\phi_1(2)\right]. $$

對 $N$ 個 electrons，一般形式是

For $N$ electrons, the general form is

$$ \Psi(1,\ldots,N)=\frac{1}{\sqrt{N!}}\mathrm{det}\begin{pmatrix}\phi_1(1)&\phi_1(2)&\cdots&\phi_1(N)\cr\phi_2(1)&\phi_2(2)&\cdots&\phi_2(N)\cr\vdots&\vdots&\ddots&\vdots\cr\phi_N(1)&\phi_N(2)&\cdots&\phi_N(N)\end{pmatrix}. $$

這就是照片下方橘色寫的 Slater determinant。

This is the Slater determinant written in orange in the lower part of the photo.

---

# 10. Exchange from antisymmetry

照片最下面的紅字想表達的是：對相同 spin 的 fermions，antisymmetric wave function 會讓兩個電子靠在完全相同 quantum state 的 amplitude 消失。

The red annotation at the bottom of the photo indicates that for same-spin fermions, antisymmetry makes the amplitude vanish when two electrons try to occupy the same one-particle quantum state.

當交換兩個相同 fermions 時，wave function 變號：

When two identical fermions are exchanged, the wave function changes sign:

$$ \Psi(1,2)=-\Psi(2,1). $$

這個 purely quantum-mechanical effect 就是 exchange physics 的來源。

This purely quantum-mechanical effect is the origin of exchange physics.

因此 Hartree mean field 只包含 classical average Coulomb repulsion，還沒有包含 fermionic exchange。

Therefore, the Hartree mean field contains only the classical average Coulomb repulsion and does not yet include fermionic exchange.

---

# 11. Hartree plus exchange–correlation picture

照片中間最後把 mean-field picture 延伸成：

The middle of the photo finally extends the mean-field picture to

$$ V_{\mathrm{eff}}(\mathbf r)=V_{\mathrm{ext}}(\mathbf r)+V_H(\mathbf r)+V_{xc}(\mathbf r). $$

其中 Hartree term 是

The Hartree term is

$$ V_H(\mathbf r)=\int d^{3}\mathbf r'\frac{n(\mathbf r')}{\lvert\mathbf r-\mathbf r'\rvert}. $$

$V_{xc}$ 則用來描述 Hartree mean field 沒有包含的 exchange 和 correlation effects。

$V_{xc}$ describes exchange and correlation effects that are not contained in the Hartree mean field.

因此原本 complicated 的 many-electron problem 被映射成 effective single-electron equations：

Therefore, the original complicated many-electron problem is mapped onto effective single-electron equations:

$$ \left[-\frac{\nabla^{2}}{2}+V_{\mathrm{ext}}(\mathbf r)+V_H(\mathbf r)+V_{xc}(\mathbf r)\right]\phi_i(\mathbf r)=\varepsilon_i\phi_i(\mathbf r). $$

這就是從 many-body problem 到 Kohn–Sham-like single-electron picture 的核心。

This is the central idea behind the mapping from the many-body problem to a Kohn–Sham-like single-electron picture.

---

# 12. Logic of the whole note

這份筆記和照片註解合起來之後，完整邏輯是：

The full logic after combining the original notes with the photo annotations is:

1. 真正的 electronic Hamiltonian 包含 electron–electron two-body Coulomb interaction。
2. 因為 $1/\lvert\mathbf r_i-\mathbf r_j\rvert$ 同時依賴兩個電子座標，不同電子 degrees of freedom 被 coupling。
3. 因此真正 wave function 是 $\Psi(\mathbf r_1\sigma_1,\ldots,\mathbf r_N\sigma_N)$，不能一般性地寫成獨立 orbitals 的 simple product。
4. 如果沒有 electron–electron interaction，Hamiltonian 可以拆成 $\sum_i h_i$，wave function 也可以用 product state separation。
5. 加入 two-body interaction 後，simple separability 被破壞。
6. mean-field approximation 把 two-body interaction 改寫成每一個電子感受到的 effective one-electron potential。
7. Hartree potential $V_H$ 是由平均 electron density 產生的 classical Coulomb field。
8. 但是電子是 fermions，所以 many-electron wave function 還必須 antisymmetric。
9. Slater determinant 自動滿足 fermionic antisymmetry。
10. antisymmetry 帶來 exchange physics，因此 Hartree term alone 不夠。
11. effective single-electron picture 最後包含 $V_{\mathrm{ext}}+V_H+V_{xc}$。
12. 因此整個目標是把 difficult many-body problem 映射成可以實際計算的 effective single-electron equations。
