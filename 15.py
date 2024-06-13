import numpy as np
student_scores=np.array([
[90,88,91,92],
[76,88,80,90],
[77,88,90,78],
[78,88,87,89]])
avg=np.mean(student_scores,axis=0)
high=np.argmax(avg)
highest= [&#39;Math&#39;, &#39;Science&#39;, &#39;English&#39;, &#39;History&#39;][high]
print(avg)
print(highest)
