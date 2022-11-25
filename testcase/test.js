function a()
{


    for (const i = 5; function(){}; i++)
    {
        try {
            break;

        catch(e)
        {
            if (false)
            {
                break;
            }
        }

        finally
        {
            while(false)
            {
                continue;
            }
        }
    }
}

