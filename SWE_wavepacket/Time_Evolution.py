## This code computes the time-evolution of an initial state in presence of a harmonic interaction
## given by the potential energy function V(x) = (m * omega**2 * x**2)/2 
## Length coordinate is in units of l0 = sqrt(hbar/(m*omega)) and energy is measured in units of E0 = hbar*omega/2. In these 
## units, the eigenvalue equation is:
###  -psi'' + (x**2)*psi = E*psi 
### where psi is the eigenfunction and E is the eigenvalue.
### The eigenvalues and eigenvectors are determined and the initial state is expressed as a linear
# superposition of these states. The time-evolution is now trivial, and the time-evolved 
# probability distribution is observed as an animation. .

import numpy as np  ## Imports module 'numpy' and uses alias 'np' to use it.
from numpy import linalg as lin   ## imports 'linalg' (a linear algebra module) and uses alias 'lin' to use it.
from matplotlib import pyplot as plt
from matplotlib import animation # Animation module.


 
delta = 0.1   ## Lattice spacing.
endpoint = 6.0 ## Lattice extends from x = -6.0 to+ 6.0
N = 60 
dimension = 2*N + 1 # Number of lattice points.


def kronecker(i,j):   ### The Kronecker Delta function.
    if i == j:
        return 1
    else:
        return 0
        
def h(i,j):  ### This defines the matrix element of the discretized Hamiltonian operator for this interaction 
    return (-kronecker(i+1,j) + 2*kronecker(i,j) - kronecker(i-1,j))/delta**2 + delta**2 * i**2 * kronecker(i,j)
    
    
H = np.array( [[h(i,j) for i in range(-N,N+1)] for j in range(-N,N+1)] )  ## Constructs the Hamiltonian matrix from its matrix elements.
# print(H)
H_eigenvalues, H_eigenvectors = lin.eig(H)  ## H_eigenvalues stores the eigenvalues and H_eigenvectors stores the eigenvectors as columns.
idx = H_eigenvalues.argsort()  ### These three lines sort the eigenvalues and eigenvectors in order of increasing eigenvalues.
H_eigenvalues = H_eigenvalues[idx]
H_eigenvectors = H_eigenvectors[:,idx]

###### The initial Gaussian wavefunction ##########
a = 1.0 ## Initial spread in units of l0
b = 0.0 ## Initial peak of the Gaussian
p0 = -2.0 ## Initial momentum in units of hbar/l0

def psi0(y):
   return (1/pow(np.pi*(a**2),0.25))*np.exp(-((y-b)**2)/(2.0*a**2) - 1j*p0*y)
    




#b = 2.0

#def psi0(y):
#   return (1/pow(np.pi,0.25))*np.exp(-((y-b)**2)/2.0)
    

Psi0 = np.sqrt(delta)*np.array( [psi0(delta*i) for i in range(-N,N+1)], 'complex' )
plt.plot (np.absolute(Psi0))
plt.show()




#################### Time evolving state  ################################

def Psi(t):
	sum = np.zeros(dimension, 'complex')
	for n in range(dimension):
		c = np.vdot(Psi0, H_eigenvectors[:,n]) # nth expansion coefficient 
		E = H_eigenvalues[n]
		sum += c * np.exp(-E*t*1.0j) * H_eigenvectors[:,n]
	return sum

def Prob(t):
    return np.array( [abs(Psi(t)[i])**2 for i in range(dimension)] )

u = np.linspace(-6, 6, 2*N+1,endpoint=True)
v = 0.003*u**2  
fig = plt.figure()
ax = plt.axes(xlim=(-6,6), ylim=(0,0.2))
line, = ax.plot([], [], lw=2)
plt.plot(u,v)

def init():
    line.set_data([], [])
    return line,


def animate(i):
    x = np.linspace(-6, 6, 121)
    y = Prob(0.05*i)
    line.set_data(x, y) 
    return line,


    
    
    
    
    
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=200, blit=True)

                             
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
                                                                                       
plt.show()
