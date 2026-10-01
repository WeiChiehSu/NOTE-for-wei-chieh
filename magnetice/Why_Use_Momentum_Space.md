# Why use momentum space? Plane-wave basis and the Kohn–Sham matrix

這份筆記的核心問題是：為什麼 plane-wave DFT 喜歡在 momentum space / reciprocal space 中工作？

The central question of these notes is: Why is momentum space / reciprocal space convenient in plane-wave DFT?

主線是：

The logical chain is:

```text
plane-wave basis
→ kinetic operator becomes diagonal
→ periodic potential is expanded by Fourier components
→ potential matrix element becomes one Fourier coefficient
→ the potential couples plane waves whose wave vectors differ by Q
→ Kohn–Sham equation becomes a matrix eigenvalue problem
```

---

# 1. Plane-wave basis

對固定的 crystal momentum $\mathbf k$，plane-wave basis 可以寫成

For a fixed crystal momentum $\mathbf k$, the plane-wave basis can be written as

$$ \langle\mathbf r\vert\mathbf G\rangle=\frac{1}{\sqrt{\Omega}}e^{i(\mathbf k+\mathbf G)\cdot\mathbf r}. $$ 

這裡 $\mathbf G$ 是 reciprocal lattice vector，而 $\Omega$ 是 normalization volume。  

Here, $\mathbf G$ is a reciprocal lattice vector and $\Omega$ is the normalization volume. 

Kohn–Sham Hamiltonian 可以分成 kinetic part 和 potential part： 

The Kohn–Sham Hamiltonian can be separated into kinetic and potential parts: 

$$ \hat H=\hat T+\hat V. $$ 其中  where $$ \hat T=-\frac{\hbar^{2}}{2m}\nabla^{2}. $$ 

---  

# 2. Why the kinetic-energy operator is simple in a plane-wave basis  

先讓 kinetic operator 作用在一個 plane wave 上： 

First apply the kinetic-energy operator to a plane wave: 

$$ \hat T\langle\mathbf r\vert\mathbf G\rangle=-\frac{\hbar^{2}}{2m}\nabla^{2}\left[\frac{1}{\sqrt{\Omega}}e^{i(\mathbf k+\mathbf G)\cdot\mathbf r}\right]. $$ 

因為 plane wave 對空間做二次微分只會產生一個 multiplicative factor：  

Because taking the second spatial derivative of a plane wave only produces a multiplicative factor, 

$$ \nabla^{2}e^{i(\mathbf k+\mathbf G)\cdot\mathbf r}=-\lvert\mathbf k+\mathbf G\rvert^{2}e^{i(\mathbf k+\mathbf G)\cdot\mathbf r}. $$ 

所以  

Therefore, 

$$ \hat T\langle\mathbf r\vert\mathbf G\rangle=\frac{\hbar^{2}}{2m}\lvert\mathbf k+\mathbf G\rvert^{2}\langle\mathbf r\vert\mathbf G\rangle. $$ 

也就是說，每一個 plane wave 本身就是 kinetic-energy operator 的 eigenstate。  

This means that every plane wave is itself an eigenstate of the kinetic-energy operator.  

對應的 eigenvalue 是  

The corresponding eigenvalue is 

$$ E_{\mathrm{kin}}(\mathbf k+\mathbf G)=\frac{\hbar^{2}}{2m}\lvert\mathbf k+\mathbf G\rvert^{2}. $$ 

這就是在 momentum space 中 kinetic term 特別簡單的第一個原因。
This is the first reason why the kinetic term is especially simple in momentum space. 

---  # 3. 

Kinetic-energy matrix element  

接著檢查 kinetic-energy matrix element 是否是 diagonal。  Next, check whether the kinetic-energy matrix element is diagonal.  定義  Define $$ T_{\mathbf G'\mathbf G}=\langle\mathbf G'\vert\hat T\vert\mathbf G\rangle. $$ 因為 $\vert\mathbf G\rangle$ 是 $\hat T$ 的 eigenstate，  Because $\vert\mathbf G\rangle$ is an eigenstate of $\hat T$, $$ \hat T\vert\mathbf G\rangle=\frac{\hbar^{2}}{2m}\lvert\mathbf k+\mathbf G\rvert^{2}\vert\mathbf G\rangle. $$ 所以  Therefore, $$ T_{\mathbf G'\mathbf G}=\frac{\hbar^{2}}{2m}\lvert\mathbf k+\mathbf G\rvert^{2}\langle\mathbf G'\vert\mathbf G\rangle. $$ 不同 plane waves 彼此 orthonormal：  Different plane waves are orthonormal: $$ \langle\mathbf G'\vert\mathbf G\rangle=\delta_{\mathbf G'\mathbf G}. $$ 因此  Therefore, $$ T_{\mathbf G'\mathbf G}=\frac{\hbar^{2}}{2m}\lvert\mathbf k+\mathbf G\rvert^{2}\delta_{\mathbf G'\mathbf G}. $$ 只要 $\mathbf G'\neq\mathbf G$，Kronecker delta 就是零。  Whenever $\mathbf G'\neq\mathbf G$, the Kronecker delta is zero.  所以 kinetic-energy matrix 沒有 off-diagonal terms。  Therefore, the kinetic-energy matrix has no off-diagonal terms.  ---  # 4. Explicit form of the kinetic-energy matrix  如果 basis 依序是 $\mathbf G_1,\mathbf G_2,\ldots,\mathbf G_N$，kinetic matrix 可以寫成  If the basis is ordered as $\mathbf G_1,\mathbf G_2,\ldots,\mathbf G_N$, the kinetic matrix can be written as $$ \mathbf T=\begin{pmatrix}\frac{\hbar^{2}}{2m}\lvert\mathbf k+\mathbf G_1\rvert^{2}&0&\cdots&0\cr 0&\frac{\hbar^{2}}{2m}\lvert\mathbf k+\mathbf G_2\rvert^{2}&\cdots&0\cr \vdots&\vdots&\ddots&\vdots\cr 0&0&\cdots&\frac{\hbar^{2}}{2m}\lvert\mathbf k+\mathbf G_N\rvert^{2}\end{pmatrix}. $$ 也就是一個 diagonal matrix。  This is a diagonal matrix.  這個結果的計算優勢很直接：kinetic operator 在 real space 中是 differential operator，但是在 plane-wave momentum basis 中變成只需要乘上一個 number。  The computational advantage is direct: in real space the kinetic operator is a differential operator, while in the plane-wave momentum basis it becomes multiplication by a number.  ---  # 5. Momentum-space picture  因此，使用 plane-wave basis 其實就是在 momentum space / reciprocal space 中工作。  Therefore, using a plane-wave basis means that we are effectively working in momentum space / reciprocal space.  kinetic term 已經很簡單，接下來真正要處理的是 potential term。  The kinetic term is already simple. The next problem is the potential term.  ---  # 6. Periodic potential in a crystal  晶體中的 potential 具有 lattice periodicity：  The potential in a crystal has lattice periodicity: $$ V(\mathbf r+\mathbf R)=V(\mathbf r). $$ 因此它可以用 Fourier series 展開：  Therefore, it can be expanded in a Fourier series: $$ V(\mathbf r)=\sum_{\mathbf Q}V_{\mathbf Q}e^{i\mathbf Q\cdot\mathbf r}. $$ 這裡 $\mathbf Q$ 是 reciprocal-space wave vector。  Here, $\mathbf Q$ is a reciprocal-space wave vector.  在一維情況，可以把 periodic potential 想成  In one dimension, a periodic potential can be viewed as $$ V(x)=V_{0}+V_{1}\cos\left(\frac{2\pi x}{a}\right)+V_{2}\cos\left(\frac{4\pi x}{a}\right)+\cdots. $$ 也可以寫成 complex-exponential Fourier components。  It can also be written in terms of complex-exponential Fourier components.  ---  # 7. Why Fourier components are useful  Fourier expansion 的物理圖像是：把一個複雜的 periodic potential 分解成很多不同 spatial frequency 的 plane-wave components。  The physical picture of a Fourier expansion is that a complicated periodic potential is decomposed into plane-wave components with different spatial frequencies.  小的 $\lvert\mathbf Q\rvert$ 對應比較長的 wavelength，所以 potential 在 real space 中變化較慢。  A small $\lvert\mathbf Q\rvert$ corresponds to a longer wavelength, so the potential changes slowly in real space.  大的 $\lvert\mathbf Q\rvert$ 對應比較短的 wavelength，所以 potential 在 real space 中變化較快。  A large $\lvert\mathbf Q\rvert$ corresponds to a shorter wavelength, so the potential changes rapidly in real space.  所以 Fourier coefficient $V_{\mathbf Q}$ 告訴我們 potential 中含有多少 wave vector $\mathbf Q$ 的 spatial-frequency component。  Thus, the Fourier coefficient $V_{\mathbf Q}$ tells us how much of the spatial-frequency component with wave vector $\mathbf Q$ is contained in the potential.  ---  # 8. How to obtain the Fourier coefficient $V_{\mathbf Q}$  從  Starting from $$ V(\mathbf r)=\sum_{\mathbf G}V_{\mathbf G}e^{i\mathbf G\cdot\mathbf r}, $$ 兩邊乘上  multiply both sides by $$ e^{-i\mathbf Q\cdot\mathbf r}, $$ 再在 unit cell 上積分：  and integrate over the unit cell: $$ \int_{\Omega}d^{3}\mathbf r\,V(\mathbf r)e^{-i\mathbf Q\cdot\mathbf r}=\sum_{\mathbf G}V_{\mathbf G}\int_{\Omega}d^{3}\mathbf r\,e^{i(\mathbf G-\mathbf Q)\cdot\mathbf r}. $$ 利用 plane-wave orthogonality，  Using plane-wave orthogonality, $$ \frac{1}{\Omega}\int_{\Omega}d^{3}\mathbf r\,e^{i(\mathbf G-\mathbf Q)\cdot\mathbf r}=\delta_{\mathbf G\mathbf Q}. $$ 所以 sum 中只有 $\mathbf G=\mathbf Q$ 的 term 留下。  Therefore, only the term with $\mathbf G=\mathbf Q$ survives in the sum.  因此  Thus, $$ V_{\mathbf Q}=\frac{1}{\Omega}\int_{\Omega}d^{3}\mathbf r\,V(\mathbf r)e^{-i\mathbf Q\cdot\mathbf r}. $$ 這就是 periodic potential 的 Fourier coefficient。  This is the Fourier coefficient of the periodic potential.  ---  # 9. Potential matrix element in the plane-wave basis  現在計算 potential matrix element：  Now calculate the potential matrix element: $$ V_{\mathbf G'\mathbf G}=\langle\mathbf G'\vert\hat V\vert\mathbf G\rangle. $$ 把 plane-wave basis 代入：  Substitute the plane-wave basis: $$ V_{\mathbf G'\mathbf G}=\frac{1}{\Omega}\int_{\Omega}d^{3}\mathbf r\,e^{-i(\mathbf k+\mathbf G')\cdot\mathbf r}V(\mathbf r)e^{i(\mathbf k+\mathbf G)\cdot\mathbf r}. $$ $\mathbf k$ 在左右兩個 plane waves 中會互相抵消：  The $\mathbf k$ factors from the two plane waves cancel: $$ V_{\mathbf G'\mathbf G}=\frac{1}{\Omega}\int_{\Omega}d^{3}\mathbf r\,V(\mathbf r)e^{i(\mathbf G-\mathbf G')\cdot\mathbf r}. $$ 前面定義 Fourier coefficient：  The Fourier coefficient was defined as $$ V_{\mathbf Q}=\frac{1}{\Omega}\int_{\Omega}d^{3}\mathbf r\,V(\mathbf r)e^{-i\mathbf Q\cdot\mathbf r}. $$ 比較 exponent：  Comparing the exponents, $$ -\mathbf Q=\mathbf G-\mathbf G'. $$ 所以  Therefore, $$ \mathbf Q=\mathbf G'-\mathbf G. $$ 因此 potential matrix element 就是  Thus, the potential matrix element is $$ V_{\mathbf G'\mathbf G}=V_{\mathbf G'-\mathbf G}. $$ 這是 momentum-space 表示非常重要的結果。  This is a very important result of the momentum-space representation.  ---  # 10. Physical meaning of $V_{\mathbf G'-\mathbf G}$  potential matrix element 不再需要每次直接處理一個 complicated real-space function。  The potential matrix element no longer requires us to directly handle a complicated real-space function every time.  它只需要查詢一個 Fourier component：  It only requires one Fourier component: $$ V_{\mathbf G'-\mathbf G}. $$ 也就是說，potential 是否能把 plane wave $\mathbf G$ coupling 到 plane wave $\mathbf G'$，取決於 potential 是否含有 wave-vector difference  That is, whether the potential can couple the plane wave $\mathbf G$ to the plane wave $\mathbf G'$ depends on whether the potential contains the wave-vector difference $$ \mathbf Q=\mathbf G'-\mathbf G. $$ 對應的 Fourier component。  as a Fourier component.  ---  # 11. See the coupling directly from $V(\mathbf r)\psi(\mathbf r)$  把 potential 展開成  Expand the potential as $$ V(\mathbf r)=\sum_{\mathbf Q}V_{\mathbf Q}e^{i\mathbf Q\cdot\mathbf r}. $$ 考慮一個 plane-wave component  Consider a plane-wave component $$ e^{i(\mathbf k+\mathbf G)\cdot\mathbf r}. $$ potential 作用後：  After multiplication by the potential, $$ V(\mathbf r)e^{i(\mathbf k+\mathbf G)\cdot\mathbf r}=\sum_{\mathbf Q}V_{\mathbf Q}e^{i(\mathbf k+\mathbf G+\mathbf Q)\cdot\mathbf r}. $$ 所以原本的 wave vector  Therefore, the original wave vector $$ \mathbf k+\mathbf G $$ 會被 potential Fourier component $\mathbf Q$ coupling 到  is coupled by the potential Fourier component $\mathbf Q$ to $$ \mathbf k+\mathbf G+\mathbf Q. $$ 如果最後的 basis state 是 $\mathbf k+\mathbf G'$，那麼  If the final basis state is $\mathbf k+\mathbf G'$, $$ \mathbf k+\mathbf G'=\mathbf k+\mathbf G+\mathbf Q. $$ 所以  Therefore, $$ \mathbf Q=\mathbf G'-\mathbf G. $$ 這和前面從 matrix element 積分得到的結果完全一致。  This is exactly the same result obtained from the matrix-element integral.  ---  # 12. Potential matrix is generally not diagonal  和 kinetic term 不同，potential term 一般會產生 off-diagonal matrix elements。  Unlike the kinetic term, the potential term generally produces off-diagonal matrix elements.  因為只要  Because whenever $$ V_{\mathbf G'-\mathbf G}\neq0, $$ 即使 $\mathbf G'\neq\mathbf G$，matrix element 仍然可以非零。  the matrix element can remain nonzero even when $\mathbf G'\neq\mathbf G$.  所以 potential matrix 的一般形式可以寫成  Therefore, the potential matrix has the general form $$ \mathbf V=\begin{pmatrix}V_{\mathbf 0}&V_{\mathbf G_1-\mathbf G_2}&\cdots&V_{\mathbf G_1-\mathbf G_N}\cr V_{\mathbf G_2-\mathbf G_1}&V_{\mathbf 0}&\cdots&V_{\mathbf G_2-\mathbf G_N}\cr \vdots&\vdots&\ddots&\vdots\cr V_{\mathbf G_N-\mathbf G_1}&V_{\mathbf G_N-\mathbf G_2}&\cdots&V_{\mathbf 0}\end{pmatrix}. $$ 這個 matrix 一般不是 diagonal。  This matrix is generally not diagonal.  它的 off-diagonal elements 就代表不同 plane waves 之間的 coupling。  Its off-diagonal elements represent coupling between different plane waves.  ---  # 13. Combine kinetic and potential terms  現在把 Kohn–Sham Hamiltonian 寫成  Now write the Kohn–Sham Hamiltonian as $$ \hat H=\hat T+\hat V. $$ 對固定 $\mathbf k$，Bloch state 用 plane-wave basis 展開：  For a fixed $\mathbf k$, expand the Bloch state in the plane-wave basis: $$ \psi_{n\mathbf k}(\mathbf r)=\sum_{\mathbf G}C_{n\mathbf k}(\mathbf G)e^{i(\mathbf k+\mathbf G)\cdot\mathbf r}. $$ Kohn–Sham equation 是  The Kohn–Sham equation is $$ \hat H\psi_{n\mathbf k}=\varepsilon_{n\mathbf k}\psi_{n\mathbf k}. $$ ---  # 14. Kinetic part acting on the expansion  kinetic operator 作用在 wave function 上：  Apply the kinetic operator to the wave function: $$ \hat T\psi_{n\mathbf k}=\sum_{\mathbf G}\frac{\hbar^{2}}{2m}\lvert\mathbf k+\mathbf G\rvert^{2}C_{n\mathbf k}(\mathbf G)e^{i(\mathbf k+\mathbf G)\cdot\mathbf r}. $$ 每一個 plane-wave component 都只乘上自己的 kinetic-energy eigenvalue。  Each plane-wave component is multiplied only by its own kinetic-energy eigenvalue.  這就是 kinetic term diagonal 的意義。  This is the meaning of the diagonal kinetic term.  ---  # 15. Potential part acting on the expansion  potential part 是  The potential part is $$ V(\mathbf r)\psi_{n\mathbf k}(\mathbf r)=\left[\sum_{\mathbf Q}V_{\mathbf Q}e^{i\mathbf Q\cdot\mathbf r}\right]\left[\sum_{\mathbf G}C_{n\mathbf k}(\mathbf G)e^{i(\mathbf k+\mathbf G)\cdot\mathbf r}\right]. $$ 把兩個 sums 相乘：  Multiplying the two sums, $$ V(\mathbf r)\psi_{n\mathbf k}(\mathbf r)=\sum_{\mathbf Q,\mathbf G}V_{\mathbf Q}C_{n\mathbf k}(\mathbf G)e^{i(\mathbf k+\mathbf G+\mathbf Q)\cdot\mathbf r}. $$ 要把結果重新寫回 basis state $\mathbf k+\mathbf G'$，令  To rewrite the result in the basis state $\mathbf k+\mathbf G'$, set $$ \mathbf G'=\mathbf G+\mathbf Q. $$ 因此  Therefore, $$ \mathbf Q=\mathbf G'-\mathbf G. $$ 所以對固定 $\mathbf G'$，potential contribution 是  Thus, for a fixed $\mathbf G'$, the potential contribution is $$ \sum_{\mathbf G}V_{\mathbf G'-\mathbf G}C_{n\mathbf k}(\mathbf G). $$ ---  # 16. Final matrix equation  把 kinetic 和 potential contributions 合在一起：  Combining the kinetic and potential contributions, $$ \sum_{\mathbf G}\left[\frac{\hbar^{2}}{2m}\lvert\mathbf k+\mathbf G\rvert^{2}\delta_{\mathbf G'\mathbf G}+V_{\mathbf G'-\mathbf G}\right]C_{n\mathbf k}(\mathbf G)=\varepsilon_{n\mathbf k}C_{n\mathbf k}(\mathbf G'). $$ 因此 Hamiltonian matrix element 是  Therefore, the Hamiltonian matrix element is $$ H_{\mathbf G'\mathbf G}(\mathbf k)=\frac{\hbar^{2}}{2m}\lvert\mathbf k+\mathbf G\rvert^{2}\delta_{\mathbf G'\mathbf G}+V_{\mathbf G'-\mathbf G}. $$ 這就是 plane-wave DFT 中要 diagonalize 的 Hamiltonian matrix。  This is the Hamiltonian matrix that must be diagonalized in plane-wave DFT.  ---  # 17. Explicit Hamiltonian matrix  如果 basis 是 $\mathbf G_1,\mathbf G_2,\ldots,\mathbf G_N$，可以把 Hamiltonian 寫成  If the basis is $\mathbf G_1,\mathbf G_2,\ldots,\mathbf G_N$, the Hamiltonian can be written as $$ \mathbf H(\mathbf k)=\begin{pmatrix}\frac{\hbar^{2}}{2m}\lvert\mathbf k+\mathbf G_1\rvert^{2}+V_{\mathbf 0}&V_{\mathbf G_1-\mathbf G_2}&\cdots&V_{\mathbf G_1-\mathbf G_N}\cr V_{\mathbf G_2-\mathbf G_1}&\frac{\hbar^{2}}{2m}\lvert\mathbf k+\mathbf G_2\rvert^{2}+V_{\mathbf 0}&\cdots&V_{\mathbf G_2-\mathbf G_N}\cr \vdots&\vdots&\ddots&\vdots\cr V_{\mathbf G_N-\mathbf G_1}&V_{\mathbf G_N-\mathbf G_2}&\cdots&\frac{\hbar^{2}}{2m}\lvert\mathbf k+\mathbf G_N\rvert^{2}+V_{\mathbf 0}\end{pmatrix}. $$ kinetic part 只出現在 diagonal。  The kinetic part appears only on the diagonal.  potential 的 Fourier components 則同時出現在 diagonal 和 off-diagonal。  The Fourier components of the potential appear both on the diagonal and off the diagonal.  ---  # 18. Matrix eigenvalue problem  把 plane-wave coefficients 排成 column vector：  Arrange the plane-wave coefficients into a column vector: $$ \mathbf C_{n\mathbf k}=\begin{pmatrix}C_{n\mathbf k}(\mathbf G_1)\cr C_{n\mathbf k}(\mathbf G_2)\cr \vdots\cr C_{n\mathbf k}(\mathbf G_N)\end{pmatrix}. $$ Kohn–Sham equation 就變成  The Kohn–Sham equation becomes $$ \mathbf H(\mathbf k)\mathbf C_{n\mathbf k}=\varepsilon_{n\mathbf k}\mathbf C_{n\mathbf k}. $$ 也就是標準 matrix eigenvalue problem。  This is a standard matrix eigenvalue problem.  對每一個 $\mathbf k$ point，都要 diagonalize 對應的 Hamiltonian matrix。  For every $\mathbf k$ point, the corresponding Hamiltonian matrix must be diagonalized.  eigenvalues 是  The eigenvalues are $$ \varepsilon_{n\mathbf k}, $$ 而 eigenvectors 的 components 就是  and the components of the eigenvectors are $$ C_{n\mathbf k}(\mathbf G). $$ 因此 diagonalization 同時告訴我們 band energy 和 Bloch wave 的 plane-wave coefficients。  Therefore, diagonalization gives both the band energies and the plane-wave coefficients of the Bloch states.  ---  # 19. Why momentum space is useful  現在可以把「為什麼用 momentum space」整理成兩個主要理由。  We can now summarize the two main reasons for using momentum space.  第一，kinetic-energy operator 變成 diagonal：  First, the kinetic-energy operator becomes diagonal: $$ T_{\mathbf G'\mathbf G}=\frac{\hbar^{2}}{2m}\lvert\mathbf k+\mathbf G\rvert^{2}\delta_{\mathbf G'\mathbf G}. $$ 所以 differential operator 變成簡單的 multiplication。  Thus, a differential operator becomes a simple multiplication.  第二，periodic potential 可以用 Fourier components 表示：  Second, a periodic potential can be represented by Fourier components: $$ V_{\mathbf G'\mathbf G}=V_{\mathbf G'-\mathbf G}. $$

所以 real-space 中 complicated 的 periodic potential，到了 momentum space 只需要用 reciprocal-space Fourier coefficient 表示不同 plane waves 之間的 coupling。

Thus, a complicated periodic potential in real space is represented in momentum space by reciprocal-space Fourier coefficients that describe coupling between different plane waves.

---

# 20. Logic of the whole derivation

這份手寫筆記的完整邏輯是：

The complete logic of the handwritten notes is:

1. 選擇 plane-wave basis $\vert\mathbf G\rangle$。
2. plane wave 是 kinetic operator 的 eigenstate。
3. 因為 plane waves orthonormal，所以 kinetic matrix 只有 diagonal elements。
4. 因此 momentum space 中 kinetic term 從 differential operator 變成 multiplicative number。
5. crystal potential 是 periodic function，因此可以做 Fourier expansion。
6. Fourier coefficient $V_{\mathbf Q}$ 代表 potential 中 wave vector $\mathbf Q$ 的 spatial-frequency component。
7. 計算 potential matrix element 後得到 $V_{\mathbf G'\mathbf G}=V_{\mathbf G'-\mathbf G}$。
8. 因此 potential Fourier component $\mathbf Q$ coupling 的兩個 plane waves 滿足 $\mathbf Q=\mathbf G'-\mathbf G$。
9. kinetic matrix 是 diagonal，但 potential matrix 一般含有 off-diagonal coupling。
10. 把 Bloch state 展開成 plane waves。
11. 分別計算 kinetic 和 potential 作用後的 coefficients。
12. 得到 Hamiltonian matrix $H_{\mathbf G'\mathbf G}(\mathbf k)$。
13. 對每一個 $\mathbf k$ point 解 matrix eigenvalue problem。
14. eigenvalues 給出 $\varepsilon_{n\mathbf k}$，eigenvectors 給出 $C_{n\mathbf k}(\mathbf G)$。
