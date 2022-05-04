20220503-180911
RandomizedSearchCV(cv=3,
                   estimator=<tensorflow.python.keras.wrappers.scikit_learn.KerasClassifier object at 0x7fe392764510>,
                   n_iter=100, n_jobs=1,
                   param_distributions={'activation': ['relu', 'tanh'],
                                        'batch_size': [16, 32, 64, 128],
                                        'epochs': [50, 100, 150, 200],
                                        'filters': [64, 16, 32, 128],
                                        'inner_kernel_size': [(1, 5)],
                                        'input_shape': [(4, 64, 1)],
                                        'kernel_size': [(4, 5), (1, 5)],
                                        'loss': ['sparse_categorical_crossentropy'],
                                        'optimizer': ['Adam', 'RMSProp',
                                                      'SGD']},
                   scoring='accuracy', verbose=5)

20220503-213009
RandomizedSearchCV(cv=3,
                   estimator=<tensorflow.python.keras.wrappers.scikit_learn.KerasClassifier object at 0x00000245F69E5160>,
                   n_iter=250, n_jobs=1,
                   param_distributions={'activation': ['relu', 'tanh'],
                                        'batch_size': [16, 32, 64, 128],
                                        'epochs': [50, 100, 150, 200],
                                        'filters': [64, 16, 32, 128],
                                        'inner_kernel_size': [(1, 5)],
                                        'input_shape': [(4, 64, 1)],
                                        'kernel_size': [(4, 5), (1, 5)],
                                        'loss': ['sparse_categorical_crossentropy'],
                                        'optimizer': ['Adam', 'RMSProp',
                                                      'SGD']},
                   scoring='accuracy', verbose=1)

20220503-230906
RandomizedSearchCV(cv=2,
                   estimator=<tensorflow.python.keras.wrappers.scikit_learn.KerasClassifier object at 0x000001C93AA09B50>,
                   n_iter=250, n_jobs=1,
                   param_distributions={'activation': ['relu', 'tanh'],
                                        'batch_size': [16, 32, 64, 128],
                                        'epochs': [50, 100, 150, 200],
                                        'filters': [64, 16, 32, 128],
                                        'inner_kernel_size': [(1, 5)],
                                        'input_shape': [(4, 64, 1)],
                                        'kernel_size': [(4, 5), (1, 5)],
                                        'loss': ['sparse_categorical_crossentropy'],
                                        'optimizer': ['Adam', 'RMSProp',
                                                      'SGD']},
                   scoring='roc_auc_ovr', verbose=1)

