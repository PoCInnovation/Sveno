const fs = require('fs')

const files = [
    "src/SSCounter.svelte",
    "src/FCTest.svelte",
    "src/CCWelcome.svelte",
    "src/CCWelcome2.svelte"
]

describe("Files", () => {
    files.map((file) => {
        test(`${file} should exist`, () => {
            expect(fs.existsSync(file)).toBe(true);
        })
    })
})