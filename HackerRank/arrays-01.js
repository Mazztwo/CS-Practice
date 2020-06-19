// HackerRank
// Arrays
// Hourglass Sum

function hourglassSum(arr)
{
    let max = null;

    for (let r = 0; r <= 3; r++)
    {
        for (let c = 0; c <=3; c++)
        {
            if (max === null)
            { 
                max = calculateHg(arr, r, c); 
            }
            else
            {
                let currSum = calculateHg(arr, r, c);

                if (currSum > max) 
                { 
                    max = currSum; 
                }
                
            }
        }
    }
    
    return max;
}

function calculateHg(arr, r, c)
{
    let hourglass = arr[r][c] +  arr[r][c+1]  + arr[r][c+2]
                          + arr[r+1][c+1] + 
                 arr[r+2][c] + arr[r+2][c+1] + arr[r+2][c+2];

    return hourglass;
}

// Max should be 19
console.log(hourglassSum([[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]));


