import torch
import pandas as pd

class EvaluationFunction():
    def __init__(self, function_name:str, nskip:int, y_column_name:str):
        
        # Dict of all available evaluation functions
        evaluation_functions = {"MSE": self.MSE, "RMSE": self.RMSE,
                                "NSE": self.NSE, "MAE": self.MAE}
        
        # Selected evaluation function
        self.eval_function = evaluation_functions[function_name]
        self.nskip = nskip
        self.function_name = function_name
        self.y_column_name = y_column_name
        
    def __call__(self, y_true:torch.Tensor, y_predict:torch.Tensor) -> torch.Tensor:
        
        # Get evaluation values for each basins (key), each target variables
        eval_values = {}

        for key in y_true.keys():
            eval_values[key] = self.eval_function(y_true[key][self.nskip:,],
                                                  y_predict[key][self.nskip:,])
            
        
        df = pd.DataFrame(torch.stack(list(eval_values.values())).numpy())
        df.index = eval_values.keys()
        df.columns = [self.function_name + "_" + name 
                      for name in self.y_column_name]
        
        return df
    
    def MSE(self, ytrue:torch.Tensor, ypredict:torch.Tensor):
        mask = ~torch.isnan(ytrue)
        mse = []
        for i in range(ytrue.shape[1]):
            mse.append(torch.mean((ytrue[:,i][mask[:,i]] - 
                                   ypredict[:,i][mask[:,i]])**2))
        mse = torch.stack(mse)
        return mse


    def RMSE(self, ytrue:torch.Tensor, ypredict:torch.Tensor):
        mse = self.MSE(ytrue, ypredict)
        rmse = mse**0.5
        return rmse
    
    # Nash–Sutcliffe efficiency (NSE)
    def NSE(self, ytrue:torch.Tensor, ypredict:torch.Tensor):
        mask = ~torch.isnan(ytrue)
        
        # Sum of Square Error (sse) = sum((true-predict)^2)
        # Sum of Square Difference around mean (ssd) = sum((true-mean_true)^2)
        sse = []        
        ssd = []
        
        for i in range(ytrue.shape[1]):
            sse.append(torch.sum((ytrue[:,i][mask[:,i]] - ypredict[:,i][mask[:,i]])**2))
            ssd.append(torch.sum((ytrue[:,i][mask[:,i]] - torch.nanmean(ytrue[:,i]))**2))
        
        nse = 1.0 - torch.stack(sse)/torch.stack(ssd)
            
        return nse
       
    def MAE(self, ytrue:torch.Tensor, ypredict:torch.Tensor):
        mask = ~torch.isnan(ytrue)
        mae = []
        for i in range(ytrue.shape[1]):
            error = ytrue[:,i][mask[:,i]] - ypredict[:,i][mask[:,i]]
            mae.append(torch.mean(torch.abs(error)))
        mae = torch.stack(mae)
        
        return mae
