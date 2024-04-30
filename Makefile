setup:
	curl -sSL https://install.python-poetry.org | python3 -
install-deps:
	@poetry install --no-root --sync
	@$(poetry env use python3.12)

exercise-1:
	@poetry run python delete_columns_that_contain_a_single_value.py

exercise-2:
	@poetry run python delete_columns_with_less_than_1_percent_unique_values.py

exercise-3:
	@poetry run python remove_columns_with_low_variance.py

exercise-4:
	@poetry run python identify_rows_that_contain_duplicate_data.py

exercise-5:
	@poetry run python delete_rows_that_contain_duplicate_data.py

exercise-6:
	@poetry run python automatic_outlier_detection.py

exercise-7:
	@poetry run python missing_values.py

exercise-8:
	@poetry run python statistical_imputation.py

exercise-9:
	@poetry run python statistical_imputation_on_prediction.py

exercise-10:
	@poetry run python knn_imputation.py

exercise-11:
	@poetry run python knn_imputation_on_prediction.py

exercise-12:
	@poetry run python mutual_information_feature_selection_for_categorical_data.py

exercise-13:
	@poetry run python model_using_all_input_features.py

exercise-14:
	@poetry run python model_using_using_chi_squared_input_features.py

exercise-15:
	@poetry run python model_using_using_mutual_information_features.py

exercise-16:
	@poetry run python model_using_all_input_features_no_correlation.py

exercise-17:
	@poetry run python model_using_all_input_features_with_correlation.py

exercise-18:
	@poetry run python explore_ algorithm_wrapped_by_recursive_feature_elimination.py

exercise-19:
	@poetry run python minmax_scaler.py

exercise-20:
	@poetry run python knn_with_scaler_transform.py

exercise-21:
	@poetry run python normalization_yeo_johnson_transformation.py

exercise-22:
	@poetry run python knn_normalization.py

exercise-23:
	@poetry run python pca_dimensionality_reduction.py



