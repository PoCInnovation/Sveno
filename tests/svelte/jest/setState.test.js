import setState from "../src/setState/SSCounter.svelte"

import { render, fireEvent } from '@testing-library/svelte'
import '@testing-library/jest-dom/extend-expect'

describe("setState", () => {
    test("should render correctly", async () => {
        const { getByText } = render (setState);
        const button = getByText('Count is 0');

        expect(button).toBeInTheDocument();
    })
})

describe("setState", () => {
    test("Clicks should work", async () => {
        const { getByText } = render (setState);
        const button = getByText('Count is 0');

        await fireEvent.click(button);
        expect(button).toHaveTextContent('Count is 1')
        await fireEvent.click(button);
        await fireEvent.click(button);
        await fireEvent.click(button);
        expect(button).toHaveTextContent('Count is 4')
    })
})