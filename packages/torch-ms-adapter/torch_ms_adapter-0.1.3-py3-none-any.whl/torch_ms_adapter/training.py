from mindspore import Model
from mindspore.train.callback import LossMonitor

class Trainer:
    def __init__(self, model, optimizer, loss_fn):
        self.model = Model(model, loss_fn=loss_fn, optimizer=optimizer, metrics={'accuracy'})

    def fit(self, train_ds, test_ds, epochs=3):
        print("开始训练...")
        self.model.train(epochs, train_ds.ds, callbacks=[LossMonitor(100)], dataset_sink_mode=False)
        metrics = self.model.eval(test_ds.ds, dataset_sink_mode=False)
        print(f"测试集准确率: {metrics['accuracy']:.4f}")