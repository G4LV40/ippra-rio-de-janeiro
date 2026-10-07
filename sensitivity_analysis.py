import numpy as np, pandas as pd, sys
from scipy.stats import spearmanr
path=sys.argv[1]
V=["qi04","qa04","piaf","poea_af","idhm_e","idhm_l","idhm_r","gin","t_banagua","t_luz","assoc","icms_t","pr_af","exis","pap_pi","pap_us","pap_m","pipo","rlt","appt","aurt","bpm","reg"]
d=pd.read_excel(path,sheet_name="Dados")
def varimax(L,tol=1e-7,it=500):
    sc=np.sqrt((L**2).sum(1)); sc[sc==0]=1; N=L/sc[:,None]; p,k=N.shape; R=np.eye(k); prev=0
    for _ in range(it):
        Lr=N@R; t=N.T@(Lr**3-Lr@np.diag((Lr**2).sum(0))/p); u,s,vh=np.linalg.svd(t,full_matrices=False); R=u@vh; c=s.sum()
        if prev and c/prev<1+tol: break
        prev=c
    return (N@R)*sc[:,None]
# proper parallel analysis (same as notebook)
def pa_k(vars_):
    z=(d[vars_]-d[vars_].mean())/d[vars_].std(ddof=1); n,p=z.shape
    ev=np.sort(np.linalg.eigvalsh(z.corr().to_numpy()))[::-1]; g=np.random.default_rng(42); sim=np.empty((1000,p))
    for s in range(1000): sim[s]=np.linalg.eigvalsh(np.corrcoef(g.normal(size=(n,p)),rowvar=False))[::-1]
    return int((ev>np.quantile(sim,0.95,axis=0)).sum())
def run_ippra(vars_,k,weights="rot",scale=False):
    z=(d[vars_]-d[vars_].mean())/d[vars_].std(ddof=1); R=z.corr().to_numpy(); ev,evec=np.linalg.eigh(R); o=np.argsort(ev)[::-1]; ev=ev[o]; evec=evec[:,o]
    L=varimax(evec[:,:k]*np.sqrt(ev[:k]))
    for j in range(k):
        i=np.argmax(abs(L[:,j]))
        if L[i,j]<0: L[:,j]*=-1
    F=z.to_numpy()@L
    if scale: F=F/F.std(axis=0,ddof=1)
    w=(L**2).sum(0); w=w/w.sum() if weights=="rot" else np.ones(k)/k
    return F@w
base=run_ippra(V,4)
low=[v for v in V if v not in ("pap_m","t_banagua","reg")]
scen={"Baseline (4 components, rotated-variance weights)":base,
"Equal component weights":run_ippra(V,4,"eq"),
"Unit-variance component scores":run_ippra(V,4,"rot",True),
"Five components":run_ippra(V,5),
"Seven components (Kaiser criterion)":run_ippra(V,7),
"Excluding the three variables with MSA < 0.50":run_ippra(low,pa_k(low))}
def q(x): return pd.qcut(pd.Series(x).rank(method="first"),4,labels=False).to_numpy()
rb=pd.Series(base).rank(ascending=False); top=set(rb[rb<=10].index)
rows=[]
for k_,v in scen.items():
    r=pd.Series(v).rank(ascending=False); rows.append((k_,round(spearmanr(base,v)[0],3),len(top&set(r[r<=10].index)),round((q(base)==q(v)).mean()*100,1)))
print(pd.DataFrame(rows,columns=["scenario","spearman","top10_overlap","same_quartile_%"]).to_string(index=False)); print('k (excl low MSA):',pa_k(low))
