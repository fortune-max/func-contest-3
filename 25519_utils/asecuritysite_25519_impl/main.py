# https://asecuritysite.com/encryption/ecc_points_add_real
import sys
import ecc
import curve25519


type='Curve25519_Montgomery'
p = pow(2,255)-19
a =486662
b=1
 

n=2 # Compute nG
y=0

if (len(sys.argv)>1):
    n=int(sys.argv[1])


print("Type: ",type)

x=9 # Base point
z=(x**3 + a*(x**2) +x) % p


# if (libnum.has_sqrtmod(z,{p:1} )):
#  y=next(libnum.sqrtmod(z,{p:1}))
y=ecc.modular_sqrt(z, p)


if (y==0):
  print ("x-point is not on the curve. Please select another point. No solution for %d (mod %d)" % (z,p))
  sys.exit()


x2 = curve25519.X25519(n, x) 
z2= (x2**3+a*(x2**2)+x2)
y2=ecc.modular_sqrt(z2, p)

  
print("a=",a)
print("b=",b)
print("p=",p)
print("n=",n)


print("\nG=(",x,",",y,")")
print("nG=(",x2,",",y2,")")


print("\n=== Just checking for (x2, y2).")
print("These have to be the same, to prove that 2P is on the elliptic curve:")

print ("\nx^3+ax^2+x (mod p)=",(x2**3+a*(x2**2)+x2) % p)
print ("y^2 (mod p)=", (y2**2)%  p)