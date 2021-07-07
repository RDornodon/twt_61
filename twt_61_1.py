N=type("N",(),{'__init__':lambda s,P,p:setattr(s,"P",P)or setattr(s,"p",p)or setattr(s,"g",0)or setattr(s,"h",0),'__eq__':lambda s,o:s.p==o.p,'f':property(lambda s:s.g+s.h)})
for _ in[I:=input]*int(I()):
 W,O,C,G,f,x,n,h,w=[],[],[],[],0,*map(int,(I()+' '+I()).split());n*=x*10;h+=2
 for l in range(h):
  for c,v in enumerate(I()):
   if v in' *':W+=[(l,c)]
   if v=='*':G+=[(l,c)]
   if v=='A':O+=[N(0,(l,c))]
 while O and G:
  o,*O=sorted(O,key=lambda n:n.f);C+=[o]
  if o.p in G:f=1;break
  for Q in[N(o,q)for h, w in((-1,0),(0,-1),(1,0),(0,1))if(q:=(o.p[0]+h,o.p[1]+w))in W]:
   if Q in C:continue
   Q.g=o.g+1;Q.h=min([abs(Q.p[0]-q[0])+abs(Q.p[1]-q[1])for q in G])
   if Q in O:q=O.index(Q);V=O[q];O[q]=[V,Q][V.f>Q.f]
   elif Q.f<=n:O.append(Q)
 print(['false','true'][f])
