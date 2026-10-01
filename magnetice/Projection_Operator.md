# Projection operator and orbital-projected weight

這份筆記的主線是：如果一個 Kohn–Sham Bloch state 同時包含很多 orbital characters，例如 $s$、$p$、$d$，那麼可以定義一個 projection operator，把 Bloch state 投影到某一個 orbital subspace，進而得到該 orbital character 在這個 Bloch state 中的 weight。

The main idea of these notes is that a Kohn–Sham Bloch state can contain several orbital characters, such as $s$, $p$, and $d$. A projection operator can be used to project the Bloch state onto a chosen orbital subspace, and the corresponding projected weight tells us how much of that orbital character is contained in the Bloch state.

整體邏輯是：

The logical chain is:

```text
choose a localized orbital subspace
→ construct the projection operator
→ apply it to a Bloch state
→ calculate the projected weight
→ interpret the weight as orbital character
→ connect the result to orbital-projected band or DOS analysis
```

---

# 1. Projection operator for a $d$-orbital subspace

手寫筆記先以 $d$ orbital subspace 為例。

The handwritten notes first use a $d$-orbital subspace as an example.

對 $d$ orbitals，

For $d$ orbitals,

$$ l=2. $$

因此 magnetic quantum number 是

Therefore, the magnetic quantum number is

$$ m=-2,-1,0,1,2. $$

如果 localized basis states 記成

If the localized basis states are denoted by

$$ \lvert\chi_{dm}\rangle, $$

那麼投影到整個 $d$ subspace 的 projection operator 可以寫成

then the projection operator onto the full $d$ subspace can be written as

$$ \hat P_d=\sum_{m=-2}^{2}\lvert\chi_{dm}\rangle\langle\chi_{dm}\rvert. $$

這個 operator 的作用是：只保留 wave function 中位在 $d$-orbital subspace 裡的部分。

The role of this operator is to keep only the part of the wave function that lies inside the $d$-orbital subspace.

---

# 2. Projected strength

對一個 Bloch Kohn–Sham state

For a Bloch Kohn–Sham state

$$ \lvert\psi_{n\mathbf k}\rangle, $$

手寫筆記把 $d$-projected strength 寫成

the handwritten notes write the $d$-projected strength as

$$ W_d(n,\mathbf k)=\langle\psi_{n\mathbf k}\vert\hat P_d\vert\psi_{n\mathbf k}\rangle. $$

把 $\hat P_d$ 的定義代入：

Substitute the definition of $\hat P_d$:

$$ W_d(n,\mathbf k)=\left\langle\psi_{n\mathbf k}\left\vert\sum_{m=-2}^{2}\lvert\chi_{dm}\rangle\langle\chi_{dm}\rvert\right\vert\psi_{n\mathbf k}\right\rangle. $$

把 summation 拆開：

Expanding the summation,

$$ W_d(n,\mathbf k)=\sum_{m=-2}^{2}\langle\psi_{n\mathbf k}\vert\chi_{dm}\rangle\langle\chi_{dm}\vert\psi_{n\mathbf k}\rangle. $$

因為

Because

$$ \langle\psi_{n\mathbf k}\vert\chi_{dm}\rangle=\left[\langle\chi_{dm}\vert\psi_{n\mathbf k}\rangle\right]^{\ast}, $$

所以

Therefore,

$$ W_d(n,\mathbf k)=\sum_{m=-2}^{2}\lvert\langle\chi_{dm}\vert\psi_{n\mathbf k}\rangle\rvert^{2}. $$

這就是手寫筆記中 projected strength 的公式。

This is the projected-strength formula written in the notes.

---

# 3. Physical meaning of $W_d$

$W_d$ 表示 Bloch state 中有多少 weight 落在 selected $d$-orbital subspace。

$W_d$ measures how much of the Bloch state lies inside the selected $d$-orbital subspace.

如果

If

$$ W_d\approx1, $$

代表這個 Bloch state 幾乎完全是 $d$ character。

the Bloch state is almost entirely $d$-like.

如果

If

$$ W_d\approx0, $$

代表這個 Bloch state 幾乎沒有 $d$ character。

the Bloch state has almost no $d$ character.

如果介於兩者之間，就代表這個 Bloch state 是混合 orbital character。

If the value lies between 0 and 1, the Bloch state contains mixed orbital character.

---

# 4. Expand a Bloch state in orbital characters

手寫筆記把一個 Bloch state 概念性地寫成

The handwritten notes write a Bloch state conceptually as

$$ \lvert\psi_{n\mathbf k}\rangle=a_s\lvert s\rangle+a_p\lvert p\rangle+a_d\lvert d\rangle+\cdots. $$

這表示同一個 Bloch state 可能同時包含 $s$、$p$、$d$ 等不同 orbital contributions。

This means that one Bloch state may contain $s$, $p$, $d$, and other orbital contributions at the same time.

對應的 projected weights 可以理解成

The corresponding projected weights can be understood as

$$ W_s\sim\lvert a_s\rvert^{2}, $$

$$ W_p\sim\lvert a_p\rvert^{2}, $$

以及

and

$$ W_d\sim\lvert a_d\rvert^{2}. $$

所以 projected band structure 或 projected DOS 中看到的 orbital weight，本質上就是在問 Bloch state 對某個 orbital subspace 的 projection 有多大。

Therefore, the orbital weight shown in a projected band structure or projected DOS essentially measures how strongly the Bloch state projects onto a chosen orbital subspace.

---

# 5. Simple example of orbital weights

筆記舉的例子是

The notes give an example such as

$$ W_d=0.90, $$

$$ W_p=0.08, $$

$$ W_s=0.02. $$

這表示該 Bloch state 主要是 $d$ character，同時帶有少量 $p$ 和 $s$ character。

This means that the Bloch state is mainly $d$-like, with smaller $p$ and $s$ contributions.

---

# 6. Why the projection weight has this form

如果一個 state 是

Suppose a state is

$$ \lvert\psi\rangle=a\lvert 1\rangle+b\lvert 2\rangle+c\lvert 3\rangle, $$

而 $\lvert1\rangle$、$\lvert2\rangle$、$\lvert3\rangle$ 是 orthonormal basis states。

and $\lvert1\rangle$, $\lvert2\rangle$, and $\lvert3\rangle$ are orthonormal basis states.

投影到 $\lvert1\rangle$ 的 amplitude 是

The projection amplitude onto $\lvert1\rangle$ is

$$ \langle1\vert\psi\rangle=a. $$

所以對應的 weight 是

Therefore, the corresponding weight is

$$ \lvert\langle1\vert\psi\rangle\rvert^{2}=\lvert a\rvert^{2}. $$

這就是為什麼 projection strength 最後會出現 overlap amplitude 的 absolute square。

This is why the projection strength is the absolute square of the overlap amplitude.

---

# 7. Connect the orbital expansion to a Hamiltonian matrix

手寫筆記接著用一個 $s$、$p$、$d$ basis 的 Hamiltonian matrix 來理解 orbital mixing。

The handwritten notes then use a Hamiltonian matrix in an $s$-$p$-$d$ basis to understand orbital mixing.

可以寫成

It can be written as

$$ \mathbf H=\begin{pmatrix}\varepsilon_s&H_{sp}&H_{sd}\cr H_{ps}&\varepsilon_p&H_{pd}\cr H_{ds}&H_{dp}&\varepsilon_d\end{pmatrix}. $$

basis vector 可以寫成

The basis vector can be written as

$$ \begin{pmatrix}\lvert s\rangle\cr\lvert p\rangle\cr\lvert d\rangle\end{pmatrix}. $$

---

# 8. Meaning of diagonal and off-diagonal elements

Hamiltonian 的 diagonal terms 是

The diagonal terms of the Hamiltonian are

$$ \varepsilon_s,\qquad\varepsilon_p,\qquad\varepsilon_d. $$

它們代表在這個 basis 中，各 orbital 本身對應的 energy。

They represent the energies associated with the individual orbitals in this basis.

off-diagonal terms 例如

Off-diagonal terms such as

$$ H_{sp},\qquad H_{sd},\qquad H_{pd} $$

代表不同 orbital basis states 之間的 coupling。

represent the coupling between different orbital basis states.

如果 off-diagonal elements 不為零，eigenstate 一般不會是純粹的 $\lvert s\rangle$、$\lvert p\rangle$ 或 $\lvert d\rangle$。

If the off-diagonal elements are nonzero, the eigenstate is generally not a pure $\lvert s\rangle$, $\lvert p\rangle$, or $\lvert d\rangle$ state.

而會是線性組合：

Instead, it becomes a linear combination:

$$ \lvert\psi\rangle=a\lvert s\rangle+b\lvert p\rangle+c\lvert d\rangle. $$

因此 orbital projection 的作用就是分析 eigenvector 裡每一個 orbital component 有多大。

Therefore, orbital projection analyzes the size of each orbital component in the eigenvector.

---

# 9. Diagonal Hamiltonian as a simple limit

如果不同 orbitals 完全沒有 coupling，

If the different orbitals are completely uncoupled,

$$ H_{sp}=H_{sd}=H_{pd}=0, $$

那麼 Hamiltonian 變成 diagonal：

then the Hamiltonian becomes diagonal:

$$ \mathbf H=\begin{pmatrix}\varepsilon_s&0&0\cr 0&\varepsilon_p&0\cr 0&0&\varepsilon_d\end{pmatrix}. $$

這時 eigenstates 就可以直接是純粹的 orbital basis states。

In this case, the eigenstates can be pure orbital basis states.

例如

For example,

$$ \lvert\psi_1\rangle=\lvert s\rangle, $$

$$ \lvert\psi_2\rangle=\lvert p\rangle, $$

$$ \lvert\psi_3\rangle=\lvert d\rangle. $$

此時 projection weight 會是非常直接的 0 或 1。

The projection weights are then simply 0 or 1.

---

# 10. Off-diagonal coupling creates orbital mixing

在真正材料中，off-diagonal coupling 通常不會全部是零。

In a real material, the off-diagonal couplings are generally not all zero.

所以一個 eigenstate 可以寫成

Therefore, an eigenstate can be written as

$$ \lvert\psi\rangle=a\lvert s\rangle+b\lvert p\rangle+c\lvert d\rangle. $$

對這個 state，

For this state,

$$ W_s=\lvert a\rvert^{2}, $$

$$ W_p=\lvert b\rvert^{2}, $$

$$ W_d=\lvert c\rvert^{2}. $$

如果 basis 是 normalized 且完整，

If the basis is normalized and complete,

$$ W_s+W_p+W_d=1. $$

這就是筆記中從 Hamiltonian matrix 連到 orbital weights 的直觀圖像。

This is the intuitive picture connecting the Hamiltonian matrix to orbital weights in the notes.

---

# 11. Projection operator as a subspace selector

如果我們只關心 $d$ subspace，

If we only care about the $d$ subspace,

$$ \hat P_d=\sum_{m=-2}^{2}\lvert\chi_{dm}\rangle\langle\chi_{dm}\rvert. $$

這個 operator 可以看成一個 subspace selector。

This operator can be viewed as a subspace selector.

它作用在一個含有很多 orbital components 的 Bloch state 上，只保留 $d$-orbital part。

When it acts on a Bloch state containing many orbital components, it keeps only the $d$-orbital part.

因此

Therefore,

$$ \hat P_d\lvert\psi_{n\mathbf k}\rangle $$

就是 Bloch state 在 $d$ subspace 中的 projected component。

is the projected component of the Bloch state inside the $d$ subspace.

---

# 12. Projected amplitude and projected weight

projected amplitude 本身仍然是一個 state：

The projected amplitude is still a state:

$$ \hat P_d\lvert\psi_{n\mathbf k}\rangle. $$

它的 norm squared 是

Its norm squared is

$$ \langle\psi_{n\mathbf k}\vert\hat P_d^{\dagger}\hat P_d\vert\psi_{n\mathbf k}\rangle. $$

對 projection operator，

For a projection operator,

$$ \hat P_d^{\dagger}=\hat P_d, $$

而且

and

$$ \hat P_d^{2}=\hat P_d. $$

所以

Therefore,

$$ \langle\psi_{n\mathbf k}\vert\hat P_d^{\dagger}\hat P_d\vert\psi_{n\mathbf k}\rangle=\langle\psi_{n\mathbf k}\vert\hat P_d\vert\psi_{n\mathbf k}\rangle. $$

也就是

That is,

$$ W_d(n,\mathbf k)=\langle\psi_{n\mathbf k}\vert\hat P_d\vert\psi_{n\mathbf k}\rangle. $$

---

# 13. QE and VASP projection bases in the handwritten notes

手寫筆記最後特別記下兩種 code 的 projection basis。

At the end, the handwritten notes record the projection bases used by two codes.

對 Quantum ESPRESSO，筆記寫的是

For Quantum ESPRESSO, the notes state

```text
Löwdin-orthogonalized atomic wavefunction
```

對 VASP，筆記寫的是

For VASP, the notes state

```text
PAW projection function
```

也就是說，兩個 code 都可以計算 orbital-projected weight，但實際使用的 projector / localized basis 定義不完全相同。

This means that both codes can calculate orbital-projected weights, but the detailed definitions of their projectors or localized basis functions are not identical.

---

# 14. Meaning of comparing QE and VASP orbital weights

筆記最後用

The notes end with the idea

$$ W_l^{\mathrm{QE}}\sim W_l^{\mathrm{VASP}}. $$

這裡的意思是：兩邊都在描述某個 angular-momentum channel $l$ 的 orbital character。

The meaning is that both codes are describing the orbital character of an angular-momentum channel $l$.

但是因為 projector construction 不同，實際 numerical value 的定義基礎並不完全相同。

However, because the projector construction is different, the detailed numerical definition is not exactly the same.

---

# 15. Logic of the whole derivation

這份手寫筆記的完整邏輯是：

The complete logic of the handwritten notes is:

1. 選擇一個 localized orbital subspace，例如 $d$ orbitals。
2. 對 $d$ subspace 定義 projection operator $\hat P_d=\sum_m\lvert\chi_{dm}\rangle\langle\chi_{dm}\rvert$。
3. 把 Bloch Kohn–Sham state 投影到這個 subspace。
4. projected strength 寫成 $W_d=\langle\psi\vert\hat P_d\vert\psi\rangle$。
5. 展開 projector 後得到 $W_d=\sum_m\lvert\langle\chi_{dm}\vert\psi\rangle\rvert^{2}$。
6. Bloch state 可以同時包含 $s$、$p$、$d$ 等不同 orbital characters。
7. projected weight 可以理解成對應 orbital coefficient 的 absolute square。
8. Hamiltonian diagonal elements 描述各 orbital basis energy。
9. off-diagonal Hamiltonian elements 造成不同 orbital basis states 之間的 mixing。
10. 因此真正的 eigenstate 一般是多個 orbital basis states 的線性組合。
11. projection operator 用來量出 eigenstate 中指定 orbital subspace 的 weight。
12. QE 筆記中使用 Löwdin-orthogonalized atomic wavefunctions 作為 projection basis。
13. VASP 筆記中使用 PAW projection functions。
14. 兩者都描述 orbital character，但 projector definition 不完全相同。
