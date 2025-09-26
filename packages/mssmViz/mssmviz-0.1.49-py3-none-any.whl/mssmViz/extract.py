from .sim import np, pd
from mssm.models import *  # noqa: F403

######## Contains functions to extract useful information from GAMM & GAMMLSS models ######## # noqa


def eval_coverage(
    model: GAMM | GAMMLSS | GSMM,  # noqa: F405
    pred_dat: pd.DataFrame,
    dist_par: int = 0,
    target: float | list[float] = 0.0,
    use: list[int] = None,
    alpha: float = 0.05,
    whole_function: bool = False,
    n_ps: int = 10000,
    seed: int | None = None,
) -> tuple[bool, float, list[bool]]:
    """Evaluate CI coverage of ``target`` function over domain defined by ``pred_dat``.

    :param model: ``GAMM`` or ``GAMMLSS`` or ``GSMM`` model.
    :type model: GAMM or GAMMLSS or GSMM
    :param pred_dat: ``pandas.DataFrame`` with data used to compute model predictions to be
        compared against target as well as CI.
    :type pred_dat: pd.Dataframe
    :param dist_par: The index corresponding to the parameter for which to make the prediction
        (e.g., 0 = mean) - only necessary if a ``GAMMLSS`` model is provided, defaults to 0
    :type dist_par: int, optional
    :param target: Target function. Can either be set to a float (e.g., 0.0 if the target function
        is believed to be zero everywhere across the domain) or a ``list``/``np.array`` of floats.
        In the latter case the shape of ``target`` must be a flattened 1D array. Defaults to 0.0
    :type target: float or [float], optional
    :param use: The indices corresponding to the terms that should be used to obtain the prediction
        or ``None`` in which case all terms will be used.
    :type use: list[int] or None
    :param alpha: The alpha level to use for the standard error calculation. Specifically,
        ``1 - (alpha/2)`` will be used to determine the critical cut-off value according to a
        N(0,1).
    :type alpha: float, optional
    :param whole_function: Whether or not to adjuste the point-wise CI to behave like
        whole-function (based on Wood, 2017; section 6.10.2 and Simpson, 2016). Defaults to False.
    :type whole_function: bool, optional
    :param n_ps: How many samples to draw from the posterior in case the point-wise CI is adjusted
        to behave like a whole-function CI.
    :type n_ps: int, optional
    :param seed: Can be used to provide a seed for the posterior sampling step in case the
        point-wise CI is adjusted to behave like a whole-function CI.
    :type seed: int | None, optional
    :return: A tuple with three elements. First is a bool, indicating whether the target function
        is covered by the CI at every evaluated value of the domain. Second is the (average)
        coverage across the entire domain. Third is a boolean array indicating for every evaluated
        value whether the corresponding value of target falls within the CI boundaries.
    :rtype: tuple[bool, float, list[bool]]
    """

    # Compute model prediction and CI boundaries
    pred, _, b = model.predict(
        use,
        pred_dat,
        ci=True,
        whole_interval=whole_function,
        alpha=alpha,
        n_ps=n_ps,
        seed=seed,
        par=dist_par,
    )

    # Compute upper and lower boundaries
    UB = pred + b
    LB = pred - b

    # Check for how many evaluated values CI contains ground truth.
    IN_CI = (UB >= target) & (LB <= target)

    full_coverage = True  # Function covered fully?
    coverage = 1

    # Function is not covered at every value of domain by CI boundaries, re-compute coverage
    # across domain
    if False in np.unique(IN_CI):
        full_coverage = False
        coverage = np.sum(IN_CI) / len(IN_CI)

    return full_coverage, coverage, IN_CI


def get_term_coef(
    model: GAMM | GAMMLSS | GSMM, which: list[int], dist_par=0  # noqa: F405
) -> tuple[np.ndarray, np.ndarray]:
    """Get the coefficients (and their names) associated with a specific term included in the
    ``Formula`` of ``model``. Useful to extract for example the estimated random intercepts from a
    random effect model.

    Note, coefficients will be in order of the model matrix columns. For a random intercept term
    (``ri()``) this implies that the first coefficient in the returned vector will correspond to the
    first encoded level of the random factor. Usually, ``mssm`` determines the level-ordering
    automatically and the actual factor-level corresponding to the first encoded level can be
    determined by inspecting the code-book returned from ``formula.get_factor_codings()``.

    :param model: ``GAMM`` or ``GAMMLSS`` or ``GSMM`` model.
    :type model: GAMM | GAMMLSS | GSMM
    :param which: Index corresponding to the term in the model's formula for which the coefficients
        should be extracted.
    :type which: list[int]
    :param dist_par: The index corresponding to the parameter for which to make the prediction
        (e.g., 0 = mean) - only necessary if a GAMMLSS model is provided, defaults to 0
    :type dist_par: int, optional
    :return: The extracted coefficients, and their names
    :rtype: tuple[np.ndarray ,np.ndarray]
    """

    # Get model-matrix that was used for fitting.
    model_mat = model.get_mmat(use_terms=which)

    if isinstance(model, GAMM) is False:  # noqa: F405
        model_mat = model_mat[dist_par]

    # Find coefficient indices corresponding to indicated terms:
    coef_idx = model_mat.sum(axis=0) != 0

    # Return corresponding coefficients.
    if isinstance(model, GAMM) is False:  # noqa: F405

        # Get names
        all_names = []
        for form in model.formulas:
            all_names.extend(form.coef_names)

        split_coef = np.split(model.coef, model.coef_split_idx)
        split_names = np.split(all_names, model.coef_split_idx)
        return split_coef[dist_par][coef_idx], split_names[dist_par][coef_idx]
    else:
        return model.coef[coef_idx], np.array(model.formulas[0].coef_names)[coef_idx]
