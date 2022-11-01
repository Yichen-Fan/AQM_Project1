import numpy as np
import matplotlib.pyplot as plt

#preparation

localnstate=2
Nsite=2**3
Ndim=2**8
state_arr = []
this_state = []
talk = [0,1,2,3,4,5,6,7]
talk_to = [[1,3,4],[0,2,5],[3,1,6],[0,2,7],[0,7,5],[4,6,1],[5,7,2],[3,4,6]]

#Append all 256 states into state_arr
for site0 in range(localnstate):
 for site1 in range(localnstate):
  for site2 in range(localnstate):
   for site3 in range(localnstate):
    for site4 in range(localnstate):
     for site5 in range(localnstate):
      for site6 in range(localnstate):
       for site7 in range(localnstate):
         this_state.append(site0)
         this_state.append(site1)
         this_state.append(site2)
         this_state.append(site3)
         this_state.append(site4)
         this_state.append(site5)
         this_state.append(site6)
         this_state.append(site7)
         state_arr.append(this_state)
         this_state = []

#define functions
#Judge if <statem| H |staten> has hopping
def there_is_a_cross_talk(statem,staten):
  #two identical states cannot cross talk
  if (np.array(statem) == np.array(staten)).all(): return False
  #states with different particle number cannot cross talk
  if np.sum(statem) != np.sum(staten): return False
  for t in talk:
    for ele in talk_to[t]:
      for s in range(Nsite):
        temp_statem = np.delete(statem,[t,ele])
        temp_staten = np.delete(staten,[t,ele])
        if (temp_statem == temp_staten).all(): return True
  return False

#canonical density matrix
def canonicalrho(H,beta):
 eigvals, eigvecs = np.linalg.eig(H)
 return eigvecs.dot(np.diag(np.exp(-beta*eigvals))).dot(np.transpose(eigvecs))/np.sum(np.exp(-beta*eigvals))

#H, N and H_mueq0
def return_matrices(mu,tt):
 H = np.zeros([Ndim,Ndim])
 N = np.zeros([Ndim,Ndim])
 H_mueq0 = np.zeros([Ndim,Ndim])
 for m in range(Ndim):
  if m % 64 == 0: print(m/2.56,"%")
  H[m,m]=(6*tt-mu)*np.sum(state_arr[m])
  N[m,m]=np.sum(state_arr[m])
  H_mueq0[m,m]=(6*tt)*np.sum(state_arr[m])
  for n in range(Ndim):
    if there_is_a_cross_talk(state_arr[m],state_arr[n]):
      #Two ways for cross talk, since we have two hopping terms
      H[m,n]=-2*tt
      H_mueq0[m,n]=-2*tt
 return H,N,H_mueq0

#results for beta = 12 and mu=1.4
#get matrices
print("calculate H,N,H_mueq0 for mu=1.4")
H,N,H_mueq0 = return_matrices(1.4,1)

number = np.trace(np.matmul(N, canonicalrho(H,12)))
energy = np.trace(np.matmul(H_mueq0, canonicalrho(H,12)))
print("average number is:",number)
print("average energy is:",energy)

#mu very plot at beta=12
print("calculate H,N,H_mueq0 for varying mu")
nlist = []
mulist = np.linspace(0,5,51)
for mu in mulist:
 print("mu=",mu)
 H,N,H_mueq0 = return_matrices(mu,1)
 nlist.append(np.trace(np.matmul(N, canonicalrho(H,12))))
 
print("mulist:",mulist)
print("nlist:",nlist)

plt.plot(mulist,nlist)
plt.xlabel("$\mu$")
plt.ylabel("<n>")
plt.xlim(0,5)
plt.ylim(0,5)
plt.show()
