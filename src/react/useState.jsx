import React from 'react'

function counter() {

    const [count, setCount] = useState(0);

    const IncrementItem = () => {
        setCount(count + 1);
    }

        return (
            <button onClick={IncrementItem}>Count is {count}</button>
        )
}

export default counter;