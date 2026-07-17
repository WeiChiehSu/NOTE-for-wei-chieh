$$
Prove:spin-martix(2\times 2)\longrightarrow I(Unit-matrix)+\sigma (pauli-martix)
$$

$$
spin-martix:n(r)=
\begin{pmatrix}
 n_{\uparrow \uparrow } (r) &n_{\uparrow \downarrow } (r) \\
 n_{\downarrow \uparrow} (r) &n_{\downarrow \downarrow} (r)
\end{pmatrix}
\longrightarrow n(r)=
\begin{pmatrix}
 n_{\uparrow \uparrow } (r) &0 \\
 0 &n_{\downarrow \downarrow} (r)
\end{pmatrix}
$$

$$
total-density:n_{0}=n_{\uparrow \uparrow }+n_{\downarrow \downarrow};magnetic-density:m_{z}=n_{\uparrow \uparrow }-n_{\downarrow \downarrow}
$$

$$
\sigma _{0}=I=
\begin{pmatrix}
 1 &0 \\
 0 &1
\end{pmatrix}
;\sigma _{z} =
\begin{pmatrix}
 1 &0 \\
 0 &-1
\end{pmatrix} \Longrightarrow
\frac{n_{0} }{2} \sigma _{0}=I=
\begin{pmatrix}
 \frac{n_{0} }{2} &0 \\
 0 &\frac{n_{0} }{2}
\end{pmatrix}
;\frac{m_{z}  }{2}\sigma _{z} =
\begin{pmatrix}
 \frac{m_{z}  }{2} &0 \\
 0 &-\frac{m_{z}  }{2}
\end{pmatrix}
\Longrightarrow 
\frac{n_{0} }{2} \sigma _{0}+\frac{m_{z}  }{2}\sigma _{z} =
\begin{pmatrix}
 \frac{n_{0}+m_{z}  }{2} &0 \\
 0 &\frac{n_{0}-m_{z}  }{2}
\end{pmatrix}
$$

$$
n_{0}=n_{\uparrow \uparrow }+n_{\downarrow \downarrow},m_{z}= n_{\uparrow \uparrow }-n_{\downarrow \downarrow}
$$

$$
\frac{n_{0} }{2} \sigma _{0}+\frac{m_{z}  }{2}\sigma _{z} =
\begin{pmatrix}
 \frac{n_{\uparrow \uparrow }+n_{\downarrow \downarrow}+n_{\uparrow \uparrow }-n_{\downarrow \downarrow}  }{2} &0 \\
 0 &\frac{n_{\uparrow \uparrow }+n_{\downarrow \downarrow}-n_{\uparrow \uparrow }+n_{\downarrow \downarrow}  }{2}
\end{pmatrix} \Longrightarrow
\begin{pmatrix}
 n_{\uparrow \uparrow } &0 \\
 0 &n_{\downarrow \downarrow}
\end{pmatrix}
$$

$$
n(r)=
\begin{pmatrix}
 n_{\uparrow \uparrow } &0 \\
 0 &n_{\downarrow \downarrow}
\end{pmatrix}
=\frac{1}{2}[n_{0}(r)I+m_{z}\sigma _{z}]
$$
