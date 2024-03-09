/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
  let si = 0, pi = 0, start_index = -1, pointer = -1

  while (si < s.length) {
      if ((pi < p.length && s[si] === p[pi]) || p[pi] === '?') {
          si++
          pi++
      } else if (pi < p.length && p[pi] === '*') {
          start_index = pi++
          pointer = si
      } else if (start_index === -1) return false
      else {
          pi = start_index + 1
          si = ++pointer
      }
  }
  for (let i = pi; i < p.length; i++) {
      if (p[i] !== '*') return false
  }

  return true

};
