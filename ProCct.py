import procct
import inspect

try:
    print("Auto_run arguments:", inspect.signature(Tarmuxset.auto_run))
except:
    print("Signature not found. Trying main...")

# যদি main কাজ করে তবে এটিই ব্যবহার করুন
procct.main()
