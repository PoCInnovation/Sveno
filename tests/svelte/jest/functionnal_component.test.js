import Functionnal_component from "../src/functionnal_component.svelte"

import { render } from '@testing-library/svelte'
import '@testing-library/jest-dom/extend-expect'

describe("Functionnal component", () => {
    test("should render correctly", () => {
        const { getByText } = render (Functionnal_component, { name: "John" })

        expect(getByText("Bonjour, John")).toBeInTheDocument()
    })
})