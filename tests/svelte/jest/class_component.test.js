import Class_component from "../src/CCWelcome.svelte"

import { render } from '@testing-library/svelte'
import '@testing-library/jest-dom/extend-expect'

describe("Class component", () => {
    test("should render correctly", () => {
        const { getByText } = render (Class_component, { name: "John" })

        expect(getByText("Bonjour, John")).toBeInTheDocument()
    })
})