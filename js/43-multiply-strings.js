/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var multiply = function(num1, num2) {

  if (num1 === '0' || num2 === '0') return '0'

  const dp = [...Array(num1.length+num2.length)].fill(0)

  for (let i = num1.length-1; i >= 0; i--) {
      for (let j = num2.length-1; j >= 0; j--) {
          const prev_remainder = dp[i+j+1]
          const prod = num1[i] * num2[j] + prev_remainder
          const units = prod % 10
          const carry = Math.floor(prod / 10)

          dp[i+j+1] = units
          dp[i+j] += carry
      }
  }

  while (dp[0] === 0) dp.shift()
  return dp.join('')

};
