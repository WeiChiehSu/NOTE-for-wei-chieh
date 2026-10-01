# K-points and smearing in plane-wave DFT

這份筆記的主線是：對每一個 crystal momentum $\mathbf k$，Kohn–Sham equation 都會給出一組 eigenvalues 和 Bloch states；但是材料的總能量、電子密度等巨觀物理量不是來自單一 $\mathbf k$，而是來自整個 Brillouin zone 中所有 $\mathbf k$ states 的總和或積分。實際電腦不能計算無限多個 $\mathbf k$，因此要用有限的 k-point mesh 近似 Brillouin-zone integral。對 metal 而言，Fermi level 附近的 occupation 在 $0$ K 是 sharp step function，SCF 過程中很容易因為能帶微小移動而讓 occupation 在 0 和 1 之間突然跳動，所以再引入 smearing 把 sharp occupation 變成 smooth occupation。

The main idea of these notes is that for every crystal momentum $\mathbf k$, the Kohn–Sham equation gives a set of eigenvalues and Bloch states. However, macroscopic quantities such as the total energy and electron density do not come from only one $\mathbf k$ point. They come from all $\mathbf k$ states in the Brillouin zone. A computer cannot calculate infinitely many $\mathbf k$ points, so a finite k-point mesh is used to approximate the Brillouin-zone integral. For metals, the occupation near the Fermi level is a sharp step function at $0$ K. During SCF, a tiny change of an eigenvalue around $E_F$ can suddenly change the occupation between 0 and 1. Smearing is therefore introduced to replace the sharp occupation by a smooth occupation.

---

# 1. Bloch states are labelled by $\mathbf k$

Bloch wave 可以寫成

A Bloch wave can be written as

$$ \psi_{n\mathbf k}(\mathbf r)=e^{i\mathbf k\cdot\mathbf r}u_{n\mathbf k}(\mathbf r). $$

其中 $n$ 是 band index，而 $\mathbf k$ 是 crystal momentum。

Here, $n$ is the band index and $\mathbf k$ is the crystal momentum.

在 plane-wave basis 中，periodic part 可以展開成

In a plane-wave basis, the periodic part can be expanded as

$$ u_{n\mathbf k}(\mathbf r)=\sum_{\mathbf G}C_{n\mathbf k}(\mathbf G)e^{i\mathbf G\cdot\mathbf r}. $$

因此對每一個固定的 $\mathbf k$，Kohn–Sham equation 會變成一個 eigenvalue problem：

Therefore, for every fixed $\mathbf k$, the Kohn–Sham equation becomes an eigenvalue problem:

$$ H(\mathbf k)C_{n\mathbf k}=E_{n\mathbf k}C_{n\mathbf k}. $$

---

## 2. One $\mathbf k$ point gives many bands

對第一個 $\mathbf k$ point，例如 $\mathbf k_1$，可以得到

For the first $\mathbf k$ point, for example $\mathbf k_1$, we obtain

$$ E_{1\mathbf k_1},\quad E_{2\mathbf k_1},\quad E_{3\mathbf k_1},\ldots $$

對另一個 $\mathbf k$ point $\mathbf k_2$，則得到

For another $\mathbf k$ point $\mathbf k_2$, we obtain

$$ E_{1\mathbf k_2},\quad E_{2\mathbf k_2},\quad E_{3\mathbf k_2},\ldots $$

把同一個 band index $n$ 在不同 $\mathbf k$ points 的 eigenvalues 連起來，就得到 band dispersion：

Connecting the eigenvalues with the same band index $n$ over different $\mathbf k$ points gives the band dispersion:

$$ E_n(\mathbf k). $$

所以一個 $\mathbf k$ point 只告訴我們 band structure 在該 $\mathbf k$ 的資訊。

Therefore, one $\mathbf k$ point gives only the information of the band structure at that particular $\mathbf k$.

---

# 3. Why total density and total energy need all $\mathbf k$ points

手寫筆記特別強調：

The handwritten notes emphasize:

材料的 total density 和 total energy 不是只從一個 $\mathbf k$ state 得到，而是來自所有 allowed $\mathbf k$ states 的 contribution。

The total density and total energy of a material do not come from only one $\mathbf k$ state. They come from the contributions of all allowed $\mathbf k$ states.

例如電子密度可以概念性地寫成

For example, the electron density can be written conceptually as

$$ n(\mathbf r)=\sum_n\sum_{\mathbf k}f_{n\mathbf k}\lvert\psi_{n\mathbf k}(\mathbf r)\rvert^{2}. $$

其中 $f_{n\mathbf k}$ 是 state $(n,\mathbf k)$ 的 occupation weight。

Here, $f_{n\mathbf k}$ is the occupation weight of the state $(n,\mathbf k)$.

因此要得到巨觀系統的 density，需要把整個 Brillouin zone 中的 $\mathbf k$ states 全部考慮進去。

Therefore, to obtain the density of a macroscopic system, the $\mathbf k$ states over the entire Brillouin zone must be included.

---

# 4. How many allowed $\mathbf k$ points are there?

手寫筆記先用一維 lattice 來理解 allowed $\mathbf k$。

The handwritten notes first use a one-dimensional lattice to understand the allowed $\mathbf k$ values.

假設一維 lattice 有 $N$ 個 unit cells，每個 unit cell 的長度是 $a$。

Suppose a one-dimensional lattice has $N$ unit cells, each with length $a$.

總長度是

The total length is

$$ L=Na. $$

對整個長度使用 periodic boundary condition：

Apply the periodic boundary condition over the full length:

$$ \psi(x+Na)=\psi(x). $$

Bloch wave 平移 $Na$ 後會得到 phase factor：

A Bloch wave translated by $Na$ acquires a phase factor:

$$ \psi(x+Na)=e^{ikNa}\psi(x). $$

和 periodic boundary condition 比較：

Comparing with the periodic boundary condition,

$$ e^{ikNa}=1. $$

因此

Therefore,

$$ kNa=2\pi m. $$

所以 allowed $k$ values 是

Thus, the allowed $k$ values are

$$ k=\frac{2\pi m}{Na}. $$

其中 $m$ 可以取一系列整數，使得在第一 Brillouin zone 中總共有 $N$ 個獨立的 allowed $k$ values。

The integer $m$ takes the values needed to give $N$ independent allowed $k$ values in the first Brillouin zone.

因此，$N$ 個 unit cells 對應 $N$ 個 allowed $k$ states。

Thus, $N$ unit cells correspond to $N$ allowed $k$ states.

---

## 5. Distance between neighboring $k$ points

相鄰兩個 allowed $k$ values 的距離是

The spacing between two neighboring allowed $k$ values is

$$ \Delta k=\frac{2\pi}{Na}. $$

當 crystal 越來越大，

As the crystal becomes larger,

$$ N\rightarrow\infty. $$

因此

Therefore,

$$ \Delta k\rightarrow0. $$

所以在 macroscopic crystal limit 中，allowed $k$ points 會變得非常密，可以把 $k$ 當成 continuous variable。

Therefore, in the macroscopic-crystal limit, the allowed $k$ points become extremely dense and $k$ can be treated as a continuous variable.

這就是為什麼原本的 discrete sum 最後可以改寫成 Brillouin-zone integral。

This is why the original discrete sum can be rewritten as a Brillouin-zone integral.

---

# 6. From the $k$-point sum to a Brillouin-zone integral

在 macroscopic limit 中，手寫筆記把 discrete average

In the macroscopic limit, the handwritten notes replace the discrete average

$$ \frac{1}{N}\sum_{\mathbf k} $$

改寫成 Brillouin-zone average：

by a Brillouin-zone average:

$$ \frac{1}{N}\sum_{\mathbf k}\longrightarrow\frac{1}{\Omega_{\mathrm{BZ}}}\int_{\mathrm{BZ}}d^{3}\mathbf k. $$

其中 $\Omega_{\mathrm{BZ}}$ 是 Brillouin zone 的體積。

Here, $\Omega_{\mathrm{BZ}}$ is the volume of the Brillouin zone.

所以一個一般的物理量 $F(\mathbf k)$ 需要做

Therefore, a general physical quantity $F(\mathbf k)$ requires

$$ \frac{1}{\Omega_{\mathrm{BZ}}}\int_{\mathrm{BZ}}F(\mathbf k)d^{3}\mathbf k. $$

這就是「物理量需要對所有 $\mathbf k$ 積分」的意思。

This is the meaning of the statement that physical quantities must be integrated over all $\mathbf k$.

---

# 7. Density as a Brillouin-zone integral

電子密度可以從 discrete sum 寫成

The electron density can be written as a discrete sum:

$$ n(\mathbf r)=\sum_n\sum_{\mathbf k}f_{n\mathbf k}\lvert\psi_{n\mathbf k}(\mathbf r)\rvert^{2}. $$

在 macroscopic limit 中，可以寫成 Brillouin-zone integral：

In the macroscopic limit, it becomes a Brillouin-zone integral:

$$ n(\mathbf r)=\frac{1}{\Omega_{\mathrm{BZ}}}\int_{\mathrm{BZ}}d^{3}\mathbf k\sum_n f_{n\mathbf k}\lvert\psi_{n\mathbf k}(\mathbf r)\rvert^{2}. $$

所以 density 的計算需要兩件事：

Therefore, the density calculation needs two ingredients:

第一，對每一個 $\mathbf k$ 求出 Bloch states。

First, solve the Bloch states for each $\mathbf k$.

第二，把所有 $\mathbf k$ 的 contribution 做 Brillouin-zone integration。

Second, integrate the contributions over the Brillouin zone.

---

# 8. Why a computer needs finite k-points

真正的 Brillouin-zone integral 包含連續無限多個 $\mathbf k$ points。

The exact Brillouin-zone integral contains infinitely many continuous $\mathbf k$ points.

電腦不可能真的計算無限多個 $\mathbf k$。

A computer cannot calculate infinitely many $\mathbf k$ points.

所以實際上用有限個 sampling points 近似積分：

Therefore, in practice, the integral is approximated by a finite set of sampling points:

$$ \frac{1}{\Omega_{\mathrm{BZ}}}\int_{\mathrm{BZ}}F(\mathbf k)d^{3}\mathbf k\approx\sum_{j=1}^{N_k}w_jF(\mathbf k_j). $$

其中 $\mathbf k_j$ 是實際計算的 k-points，$w_j$ 是每個 k-point 的 integration weight。

Here, $\mathbf k_j$ are the k-points that are actually calculated and $w_j$ are their integration weights.

如果使用 symmetry，很多 symmetry-equivalent k-points 可以用一個 representative k-point 表示，這個 representative point 就會得到相應的 weight。

If symmetry is used, many symmetry-equivalent k-points can be represented by one representative k-point, and that representative point receives the corresponding weight.

---

# 9. Physical meaning of the k-point mesh

例如使用

For example, using

```text
12 12 12
```

的 k-point mesh，意思是用有限的三維 k-point sampling 去近似整個 Brillouin-zone integral。

means using a finite three-dimensional k-point sampling to approximate the full Brillouin-zone integral.

手寫筆記把 k-points 和 `ecutwfc` 的角色分得很清楚：

The handwritten notes distinguish the roles of k-points and `ecutwfc` clearly:

k-points 決定：

k-points determine:

```text
How many k points do I want to calculate?
```

而 `ecutwfc` 決定：

while `ecutwfc` determines:

```text
How many plane-wave components do I use for the wave function at each k point?
```

也就是說：

In other words:

k-point mesh 是在 Brillouin zone 中取樣多少個 $\mathbf k$。

The k-point mesh controls how many $\mathbf k$ points are sampled in the Brillouin zone.

`ecutwfc` 則控制每一個 $\mathbf k$ point 上 wave function 的 plane-wave basis 大小。

`ecutwfc` controls the size of the plane-wave basis used for the wave function at each $\mathbf k$ point.

這兩個收斂參數控制的是不同的 numerical approximation。

These two convergence parameters control different numerical approximations.

---

# 10. Monkhorst–Pack grid

手寫筆記用 reciprocal lattice vectors

The handwritten notes use the reciprocal lattice vectors

$$ \mathbf b_1,\quad\mathbf b_2,\quad\mathbf b_3 $$

來描述 Monkhorst–Pack k-point grid。

to describe the Monkhorst–Pack k-point grid.

如果使用 $12\times12\times12$ grid，那麼沿三個 reciprocal directions 的 spacing 可以概念性地寫成

For a $12\times12\times12$ grid, the spacings along the three reciprocal directions can be viewed as

$$ \Delta k_1\sim\frac{\lvert\mathbf b_1\rvert}{12}, $$

$$ \Delta k_2\sim\frac{\lvert\mathbf b_2\rvert}{12}, $$

以及

and

$$ \Delta k_3\sim\frac{\lvert\mathbf b_3\rvert}{12}. $$

因此 grid number 越大，k-point spacing 越小，Brillouin-zone sampling 越密。

Therefore, a larger grid number gives a smaller k-point spacing and a denser Brillouin-zone sampling.

---

# 11. Why a k-point convergence test is needed

總能量本質上也是 Brillouin-zone integration。

The total energy is also fundamentally a Brillouin-zone integral.

手寫筆記概念性地寫成

The handwritten notes write it conceptually as

$$ E_{\mathrm{tot}}=\frac{1}{\Omega_{\mathrm{BZ}}}\int_{\mathrm{BZ}}E(\mathbf k)d^{3}\mathbf k. $$

在有限 k-point sampling 中：

With finite k-point sampling:

$$ E_{\mathrm{tot}}\approx\sum_j w_jE(\mathbf k_j). $$

因此不同 k-point meshes 會給出稍微不同的 numerical integral。

Therefore, different k-point meshes give slightly different numerical approximations to the integral.

k-point convergence test 的目的就是逐漸增加 mesh density，檢查

The purpose of a k-point convergence test is to gradually increase the mesh density and check whether

$$ E_{\mathrm{tot}} $$

已經穩定。

has become stable.

如果增加 k-point mesh 之後 total energy 幾乎不再改變，就表示 Brillouin-zone integration 對這個物理量已經足夠收斂。

If increasing the k-point mesh no longer changes the total energy significantly, the Brillouin-zone integration is sufficiently converged for that quantity.

---

# 12. Occupation weight in the density

接下來 smearing 的來源，是 density 中的 occupation weight $f_{n\mathbf k}$。

The origin of smearing comes from the occupation weight $f_{n\mathbf k}$ in the density.

電子密度包含

The electron density contains

$$ n(\mathbf r)=\sum_n\int_{\mathrm{BZ}}f_{n\mathbf k}\lvert\psi_{n\mathbf k}(\mathbf r)\rvert^{2}d^{3}\mathbf k. $$

這裡 $f_{n\mathbf k}$ 決定一個 state 是否 occupied，以及 occupied 多少。

Here, $f_{n\mathbf k}$ determines whether a state is occupied and how much it is occupied.

---

# 13. Occupation at zero temperature

在 $0$ K 的理想情況，如果 eigenvalue 在 Fermi energy 以下：

At ideal $0$ K, if an eigenvalue is below the Fermi energy,

$$ \varepsilon_{n\mathbf k}<E_F, $$

則

then

$$ f_{n\mathbf k}=1. $$

如果 eigenvalue 在 Fermi energy 以上：

If an eigenvalue is above the Fermi energy,

$$ \varepsilon_{n\mathbf k}>E_F, $$

則

then

$$ f_{n\mathbf k}=0. $$

所以 occupation function 可以理解成一個 sharp step function：

Therefore, the occupation function can be viewed as a sharp step function:

$$ f(\varepsilon)=\Theta(E_F-\varepsilon). $$

---

# 14. Why an insulator is usually numerically easier

對 insulator，valence band 和 conduction band 中間有 band gap。

For an insulator, there is a band gap between the valence and conduction bands.

Fermi level 位在 gap 中。

The Fermi level lies inside the gap.

因此 occupied valence states 和 empty conduction states 很清楚地分開：

Therefore, the occupied valence states and empty conduction states are clearly separated:

$$ f_{\mathrm{valence}}=1, $$

$$ f_{\mathrm{conduction}}=0. $$

即使 k-grid 或 SCF potential 有一些小變化，只要 eigenvalues 沒有跨過 $E_F$，occupation 就不會突然改變。

Even if the k-grid or the SCF potential changes slightly, the occupations do not suddenly change as long as the eigenvalues do not cross $E_F$.

所以手寫筆記的圖像是：insulator 通常不需要像 metal 那樣依賴 smearing 來穩定 Fermi-surface occupation。

Therefore, the picture in the handwritten notes is that an insulator usually does not rely on smearing in the same way as a metal to stabilize the Fermi-surface occupation.

---

# 15. Why metals can cause SCF occupation oscillation

metal 的 band 會穿過 Fermi level：

In a metal, bands cross the Fermi level:

$$ \varepsilon_{n\mathbf k}\approx E_F. $$

假設某一次 SCF iteration 中，某個 state 的 eigenvalue 是

Suppose that in one SCF iteration, one state has

$$ \varepsilon_{n\mathbf k}=E_F-0.001\ \mathrm{eV}. $$

在 sharp $0$ K occupation 中，

With a sharp $0$ K occupation,

$$ f_{n\mathbf k}=1. $$

因此它完整 contribute 到 density：

Therefore, it contributes fully to the density:

$$ n(\mathbf r)\supset\lvert\psi_{n\mathbf k}(\mathbf r)\rvert^{2}. $$

但是下一個 SCF iteration 中，potential 稍微改變後，也許 eigenvalue 變成

In the next SCF iteration, after a small change of the potential, the eigenvalue may become

$$ \varepsilon_{n\mathbf k}=E_F+0.001\ \mathrm{eV}. $$

此時

Then

$$ f_{n\mathbf k}=0. $$

同一個 state 突然完全不 contribute 到 density。

The same state suddenly contributes nothing to the density.

---

## 16. Why this can make SCF oscillate

SCF cycle 中有一個 feedback loop：

There is a feedback loop in the SCF cycle:

```text
occupation
→ density
→ Kohn–Sham potential
→ wave functions and eigenvalues
→ new occupation
→ new density
```

如果 Fermi level 附近的 state 在 $f=0$ 和 $f=1$ 之間突然跳動，density 也會跳動。

If a state near the Fermi level suddenly switches between $f=0$ and $f=1$, the density also changes abruptly.

density 改變又會讓 Kohn–Sham potential 改變，再讓 eigenvalue 穿過 Fermi level 的方向改變。

The change in density modifies the Kohn–Sham potential, which can move the eigenvalue across the Fermi level again.

所以 SCF 有可能在兩個 occupation pattern 之間 oscillate。

Therefore, the SCF procedure can oscillate between two occupation patterns.

這就是手寫筆記引入 smearing 的主要 numerical motivation。

This is the main numerical motivation for smearing in the handwritten notes.

---

# 17. Two ways to improve the metallic integration

手寫筆記指出，處理 metal Fermi-surface 問題可以使用：

The handwritten notes indicate two ways to improve the metallic Fermi-surface treatment:

第一，更 dense 的 k-point mesh。

First, use a denser k-point mesh.

第二，使用 smearing。

Second, use smearing.

dense k-mesh 讓 Fermi surface 附近的 Brillouin-zone sampling 更細。

A dense k-mesh gives a finer sampling around the Fermi surface.

smearing 則讓 occupation 不再是突然從 1 跳到 0。

Smearing prevents the occupation from jumping abruptly from 1 to 0.

---

# 18. From a step function to a smooth occupation

在 sharp $0$ K occupation 中，

For the sharp $0$ K occupation,

如果

if

$$ \varepsilon\ll E_F, $$

則

then

$$ f=1. $$

如果

if

$$ \varepsilon\gg E_F, $$

則

then

$$ f=0. $$

在 $E_F$ 附近則是 sharp discontinuity。

Near $E_F$, there is a sharp discontinuity.

smearing 的想法是把這個 sharp step

The idea of smearing is to replace this sharp step

$$ \Theta(E_F-\varepsilon) $$

換成 smooth function

by a smooth function

$$ f_{\sigma}(\varepsilon). $$

---

## 19. Fractional occupation near the Fermi level

加入 smearing 後：

After smearing is introduced:

遠低於 Fermi level 的 states 仍然接近 fully occupied。

States far below the Fermi level remain nearly fully occupied.

遠高於 Fermi level 的 states 仍然接近 empty。

States far above the Fermi level remain nearly empty.

但是在一個大約由 $\sigma$ 控制的 energy window 中，可以有 fractional occupation：

However, inside an energy window controlled approximately by $\sigma$, fractional occupations are allowed:

$$ 0<f_{\sigma}(\varepsilon)<1. $$

因此如果 eigenvalue 只是在 $E_F$ 附近微小移動，occupation 只會小幅連續改變，而不是從 1 突然跳成 0。

Therefore, if an eigenvalue moves only slightly around $E_F$, the occupation changes smoothly instead of abruptly switching from 1 to 0.

---

# 20. Density with smearing

加入 smearing 後，Fermi-level 附近的 state 對 density 的 contribution 寫成

After introducing smearing, the contribution of a state near the Fermi level to the density is weighted as

$$ f_{\sigma}(\varepsilon_{n\mathbf k})\lvert\psi_{n\mathbf k}(\mathbf r)\rvert^{2}. $$

因此 density 變成

Therefore, the density becomes

$$ n(\mathbf r)=\sum_n\int_{\mathrm{BZ}}f_{\sigma}(\varepsilon_{n\mathbf k})\lvert\psi_{n\mathbf k}(\mathbf r)\rvert^{2}d^{3}\mathbf k. $$

smearing 的 numerical purpose 就是讓 density 對 eigenvalue 的小變動更 smooth。

The numerical purpose of smearing is to make the density vary more smoothly when the eigenvalues change slightly.

---

# 21. Fermi–Dirac smearing

手寫筆記首先寫 Fermi–Dirac occupation：

The handwritten notes first introduce the Fermi–Dirac occupation:

$$ f_{\mathrm{FD}}(\varepsilon)=\frac{1}{e^{(\varepsilon-E_F)/(k_BT)}+1}. $$

它描述 finite temperature 下電子的 occupation。

It describes the electron occupation at finite temperature.

如果把 smearing width 記成

If the smearing width is written as

$$ \sigma\sim k_BT, $$

就可以寫成

then the occupation can be written as

$$ f_{\mathrm{FD}}(\varepsilon)=\frac{1}{e^{(\varepsilon-E_F)/\sigma}+1}. $$

---

## 22. Zero-smearing limit

當

When

$$ \sigma\rightarrow0, $$

Fermi–Dirac function 會越來越陡。

the Fermi–Dirac function becomes increasingly sharp.

最後回到 $0$ K step function：

In the limit, it returns to the $0$ K step function:

$$ f_{\mathrm{FD}}(\varepsilon)\longrightarrow\Theta(E_F-\varepsilon). $$

所以 $\sigma$ 可以理解成控制 occupation transition 有多寬的參數。

Thus, $\sigma$ can be understood as a parameter controlling the width of the occupation transition.

---

# 23. Gaussian broadening of a delta function

手寫筆記接著使用 Gaussian function 來近似 delta function。

The handwritten notes next use a Gaussian function to approximate a delta function.

Gaussian-broadened delta function 可以寫成

A Gaussian-broadened delta function can be written as

$$ \delta_{\sigma}(x)=\frac{1}{\sqrt{\pi}\sigma}e^{-(x/\sigma)^{2}}. $$

當 $\sigma$ 很小時，Gaussian 很窄、很尖。

When $\sigma$ is small, the Gaussian is narrow and sharp.

當 $\sigma$ 變大時，Gaussian width 變大。

When $\sigma$ becomes larger, the Gaussian becomes broader.

在

At

$$ \sigma\rightarrow0 $$

的 limit 中，它趨近理想的 delta distribution。

it approaches the ideal delta distribution.

---

# 24. Gaussian broadening in energy

如果要把位在 $\varepsilon$ 的 sharp energy level 展寬，可以寫成

If a sharp energy level at $\varepsilon$ is broadened, we can write

$$ \delta_{\sigma}(E-\varepsilon)=\frac{1}{\sqrt{\pi}\sigma}e^{-((E-\varepsilon)/\sigma)^{2}}. $$

這表示原本集中在單一 energy 的 delta peak 被替換成 width 由 $\sigma$ 控制的 Gaussian peak。

This means that a delta peak concentrated at one energy is replaced by a Gaussian peak whose width is controlled by $\sigma$.

---

# 25. Occupation obtained from the broadened delta function

如果 occupation 是把 energy states 從 $-\infty$ 積分到 Fermi energy $E_F$，那麼 Gaussian-smeared occupation 可以寫成

If the occupation is obtained by integrating the energy states from $-\infty$ to the Fermi energy $E_F$, the Gaussian-smeared occupation can be written as

$$ f_{\sigma}(\varepsilon)=\int_{-\infty}^{E_F}\delta_{\sigma}(E-\varepsilon)dE. $$

代入 Gaussian broadening：

Substituting the Gaussian broadening,

$$ f_{\sigma}(\varepsilon)=\int_{-\infty}^{E_F}\frac{1}{\sqrt{\pi}\sigma}e^{-((E-\varepsilon)/\sigma)^{2}}dE. $$

這個積分的意義是：不再用一個完全 sharp 的 energy level 判斷 occupied 或 empty，而是先把 level 展寬，再計算 Fermi level 以下有多少 weight。

The meaning of this integral is that occupation is no longer determined by a perfectly sharp energy level. The level is first broadened, and the fraction of its weight below the Fermi level determines the occupation.

因此在 $E_F$ 附近自然得到 fractional occupation。

Therefore, fractional occupation appears naturally near $E_F$.

---

# 26. Connection between k-point sampling and smearing

k-point mesh 和 smearing 都和 Fermi-surface numerical integration 有關，但兩者處理不同問題。

Both the k-point mesh and smearing are related to numerical integration around the Fermi surface, but they address different issues.

k-point mesh 控制：

The k-point mesh controls:

```text
How densely is the Brillouin zone sampled?
```

smearing 控制：

Smearing controls:

```text
How sharply does the occupation change near the Fermi level?
```

對 metal 而言，如果 k-mesh 太 sparse，Fermi surface sampling 本身就不準。

For a metal, if the k-mesh is too sparse, the Fermi surface itself is poorly sampled.

如果 occupation 又完全 sharp，SCF 對 Fermi-level 附近的 small eigenvalue shift 會更敏感。

If the occupation is also perfectly sharp, the SCF calculation becomes even more sensitive to small eigenvalue shifts near the Fermi level.

所以手寫筆記的 numerical picture 是：metal 通常需要足夠 dense 的 k-mesh，再配合合適的 smearing。

Therefore, the numerical picture in the handwritten notes is that a metal usually needs a sufficiently dense k-mesh together with a suitable smearing.

---

# 27. Logic of the whole derivation

這份手寫筆記的完整邏輯是：

The complete logic of the handwritten notes is:

1. 每一個 $\mathbf k$ point 都有一組 Kohn–Sham eigenvalues $E_{n\mathbf k}$。
2. 把不同 $\mathbf k$ 上同一個 band $n$ 的 eigenvalues 連起來得到 $E_n(\mathbf k)$。
3. 巨觀 density 和 total energy 來自整個 Brillouin zone，而不是單一 $\mathbf k$。
4. 對一維 $N$-cell lattice 使用 periodic boundary condition，可得到 $N$ 個 allowed $k$ states。
5. 相鄰 allowed $k$ 的距離是 $\Delta k=2\pi/(Na)$。
6. 當 $N\rightarrow\infty$，$\Delta k\rightarrow0$，所以 discrete $k$ sum 變成 Brillouin-zone integral。
7. 電腦不能計算無限多個 $\mathbf k$，因此用有限的 k-point mesh 和 weights 近似積分。
8. Monkhorst–Pack grid 用 reciprocal lattice directions 建立規則的 k-point sampling。
9. k-point convergence test 是增加 mesh density 並檢查 total energy 是否穩定。
10. density 中每一個 state 都有 occupation weight $f_{n\mathbf k}$。
11. 在 $0$ K，occupation 是 sharp step function $\Theta(E_F-\varepsilon)$。
12. insulator 有 band gap，occupied 和 empty states 分隔清楚，所以 occupation 對小變化不敏感。
13. metal 的 band 穿過 $E_F$，SCF 中 eigenvalue 的微小變化可能讓 occupation 在 0 和 1 之間跳動。
14. occupation jump 會造成 density jump，進一步改變 Kohn–Sham potential，可能形成 SCF oscillation。
15. dense k-mesh 可以改善 Fermi-surface sampling。
16. smearing 把 sharp step occupation 改成 smooth occupation。
17. Fermi–Dirac smearing 可以用 $\sigma\sim k_BT$ 理解，$\sigma\rightarrow0$ 時回到 sharp step。
18. Gaussian smearing 用 finite-width Gaussian 近似 delta function。
19. Gaussian-smeared occupation 可以由 broadened delta 從 $-\infty$ 積分到 $E_F$ 得到。
20. k-point mesh 控制 Brillouin-zone sampling density；smearing 控制 Fermi-level 附近 occupation 的 smoothness。
