const fs = require('fs')

const files = [
    "src/class_component.svelte",
    "src/functionnal_component.svelte",
    "src/setState.svelte",
    "src/useState.svelte"
]

describe("Files", () => {
    files.map((file) => {
        test(`${file} should exist`, () => {
            expect(fs.existsSync(file)).toBe(true);
        })
    })
})