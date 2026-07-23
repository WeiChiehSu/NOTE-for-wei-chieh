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
\end{pmatrix}=n(r)
$$

$$
n(r)=
\begin{pmatrix}
 n_{\uparrow \uparrow } &0 \\
 0 &n_{\downarrow \downarrow}
\end{pmatrix}
=\frac{1}{2}[n_{0}(r)I+m_{z}\sigma _{z}]
$$

$$
Prove:m_{z}=Tr(n\sigma _{z})
$$

$$
n\sigma _{z}=
\begin{pmatrix}
 n_{\uparrow \uparrow } &0 \\
 0 &n_{\downarrow \downarrow}
\end{pmatrix}
\begin{pmatrix}
 1 &0 \\
 0 &-1
\end{pmatrix}=
\begin{pmatrix}
 n_{\uparrow \uparrow } &0 \\
 0 &-n_{\downarrow \downarrow}
\end{pmatrix}=m_{z}\Longrightarrow Tr(n\sigma _{z})=m_{z} 
$$

# Nocolinear system

$$
n=\frac{1}{2}(n_{0}I+m_{x}\sigma_{x}+m_{y}\sigma_{y}+m_{z}\sigma_{z})\Longrightarrow n(r)=
\begin{pmatrix}
n_{\uparrow \uparrow }    & n_{\uparrow \downarrow }   \\
n_{\downarrow \uparrow }  & n_{\downarrow \downarrow }
\end{pmatrix}
$$

$$
\sigma_{x}=
\begin{pmatrix}
0  & 1 \\
1  & 0
\end{pmatrix};
\sigma_{y}=
\begin{pmatrix}
0  & -i \\
i  & 0
\end{pmatrix};
\sigma_{z}=
\begin{pmatrix}
1  & 0 \\
0  & -1
\end{pmatrix}
$$

$$
\Longrightarrow n=\frac{1}{2} 
\begin{pmatrix}
n_{0} +m_{z}   & m_{x}-im_{y}   \\
m_{x}+im_{y}  & n_{0}-m_{z}
\end{pmatrix}\Longrightarrow 
\begin{pmatrix}
n_{\uparrow \uparrow } =\frac{n_{0}+m_{z}  }{2}    & n_{\uparrow \downarrow }=\frac{m_{x}-im_{y}}{2}   \\
n_{\downarrow \uparrow }=\frac{m_{x}+im_{y}}{2}  & n_{\downarrow \downarrow } =\frac{n_{0}-m_{z}}{2}
\end{pmatrix}
$$

$$
n_{0}=n_{\uparrow \uparrow }+n_{\downarrow \downarrow };m_{z}=n_{\uparrow \uparrow }-n_{\downarrow \downarrow };m_{x}=n_{\uparrow \downarrow }+n_{\downarrow \uparrow };m_{y}=i(n_{\uparrow \downarrow }-n_{\downarrow \uparrow }) 
$$
