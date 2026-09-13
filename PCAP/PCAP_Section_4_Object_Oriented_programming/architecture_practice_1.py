# 1. Hardened Class Object Tool

class Switch:
    def __init__(self,hostname, native_vlan):
        self.hostname = hostname
        # Name Mangling: Protects this variable from outside interference
        self.__native_vlan = native_vlan

    # 2. Hardened Logic Gate
    def validate_vlan(self):
        # Notice we must use 'self.__native.vlan' internally now
        if 1 <= self.__native_vlan <= 4094:
            return f"[+] {self.hostname}: VLAN {self.__native_vlan} is valid."
        return f"[-] {self.hostname}: CRITICAL! VLAN {self.__native_vlan} is out of bounds!"


# 3. Test the execution boundary
sw1 = Switch("Core-01", 99)

print(sw1.validate_vlan())
print(sw1._Switch__native_vlan)
# 📌 THE PCAP TRAP: Try to force a direct print of the protected variable
try:
    print(sw1.__native_vlan)
except AttributeError:
    print("[PROTECTED] Direct access to __native_vlan was blocked by the compiler!")


