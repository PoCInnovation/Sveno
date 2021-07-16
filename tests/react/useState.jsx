import React, { useEffect } from 'react'

function USCounter() {

    const [count, setCount] = useState(0);

    const IncrementItem = () => {
        setCount(count + 1);
    }

    useEffect(()=> {
        console.log(`count is now ${count}`)

        return ()=> {"Element destroyed"}
    }, [count])

    return (
        <button onClick={IncrementItem}>Count is {count}</button>
    )
}

export default Counter;