import Functionnal_component from "../src/FCTest.svelte"

import { render } from '@testing-library/svelte'
import '@testing-library/jest-dom/extend-expect'

describe("Functionnal component", () => {
    test("should render correctly", () => {
        const { getByText } = render (Functionnal_component, { name: "John" })

        expect(getByText("Salut, John")).toBeInTheDocument()
    })
})