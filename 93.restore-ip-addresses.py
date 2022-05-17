#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        n = len(s)
        def valid(ip):
            if not ip:
                return False
            if len(ip) == 1:
                return True
            if ip[0] == '0':
                return False
            return 0<=int(ip)<=255
        def dfs(idx, curr, remain):
            if idx > n:
                return
            if remain == 0 and idx == n:
                result.append('.'.join(curr))
                return
            for i in range(1,4):
                ip = s[idx:idx+i]
                if valid(ip):
                    dfs(idx+i, curr+[ip], remain-1)
        dfs(0, [],4)
        return result
# @lc code=end

