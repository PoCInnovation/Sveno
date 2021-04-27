const fs = require('fs')

const files = [
    "src/class_component.svelte",
    "src/functionnal_component.svelte"
]

describe("Files", () => {
    test("should exist", () => {
        files.map((file) => {
          console.log(file)
          expect(fs.existsSync(file)).toBe(true);
        })
    })
})