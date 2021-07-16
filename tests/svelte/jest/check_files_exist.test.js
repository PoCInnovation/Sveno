const fs = require('fs')

const files = [
    "src/class_component/CCWelcome.svelte",
    "src/class_component/CCWelcome2.svelte",
    "src/functionnal_component/FCTest.svelte",
    "src/setState/SSCounter.svelte",
    "src/useState/USCounter.svelte"
]

describe("Files", () => {
    files.map((file) => {
        test(`${file} should exist`, () => {
            expect(fs.existsSync(file)).toBe(true);
        })
    })
})