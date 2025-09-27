import cv2
import numpy as np
from skimage import measure
from skimage.draw import polygon2mask
from holocontour.image.structure_forest import generate_mask
from holocontour.contour.toolsbox import contour_mask_union, filter_contours_by_intensity
from holocontour.image.visual import plot_segmentation_result
from holocontour.image.region_growing import region_grow
from holocontour.image.processing import apply_histogram_matching, find_darkest_point, get_sharpening_kernel, erode_mask


def process_mask(img_org,
                 img,
                 avg_thresh,
                 min_contour_area,
                 seed_thresh,
                 median,
                 erode_ksize,
                 convex_hull):

    seed = find_darkest_point(img_org, generate_mask(img, use_convex_hull=convex_hull) > 0)
    seg_mask = region_grow(img, seed)

    contours = measure.find_contours(seg_mask, 0.5)
    filtered_contours = [c for c in contours if len(c) > min_contour_area]

    while True:
        outside = np.where((img < seed_thresh) & ~seg_mask)
        if len(outside[0]) == 0:
            break
        seed = (outside[0][0], outside[1][0])
        new_mask = region_grow(img, seed)
        seg_mask |= new_mask
        new_contours = measure.find_contours(new_mask, 0.5)
        filtered_contours += [c for c in new_contours if len(c) > min_contour_area]

    valid_contours = filter_contours_by_intensity(
        filtered_contours, img_org, avg_thresh, median
    )

    union = contour_mask_union(valid_contours, img_org.shape)

    outer_first = max(measure.find_contours(generate_mask(img, use_convex_hull=convex_hull), 0.5), key=len)
    init_mask_poly = polygon2mask(img_org.shape[:2], outer_first)
    eroded_init_mask = erode_mask(init_mask_poly, kernel_size=erode_ksize)
    outer = max(measure.find_contours(eroded_init_mask, 0.5), key=len)

    init_mask_poly = polygon2mask(img_org.shape[:2], outer)
    union &= init_mask_poly

    final_mask = np.zeros_like(union, dtype=np.uint8)
    final_contours = []

    for contour in measure.find_contours(union, 0.5):
        if len(contour) > min_contour_area:
            mask = polygon2mask(img_org.shape[:2], contour).astype(np.uint8)
            final_mask += mask
            final_contours.append(contour)

    return final_mask, final_contours, outer


def find_contours(img_org,
                 avg_thresh=81,
                 max_attempts=5,
                 increase_avg=5,
                 min_contour_area=30,
                 seed_thresh=45,
                 save_plot=False,
                 median=False,
                 hist_match=False,
                 ref_path=None,
                 erode_ksize=3,
                 convex_hull=False,
                 keep_init_mask=False,
                 median_blur_ksize=5,
                 sharpening_alpha=0):

    img = img_org.copy()

    if hist_match and ref_path:
        img = apply_histogram_matching(img_org, ref_path)

    blur = cv2.GaussianBlur(img, (3, 3), 0)
    img = cv2.addWeighted(img, 1 + sharpening_alpha, blur, -sharpening_alpha, 0)

    if median_blur_ksize > 1:
        img = cv2.medianBlur(img, median_blur_ksize)

    init_mask = generate_mask(img, use_convex_hull=convex_hull)

    if np.count_nonzero(init_mask) == 0:
        print("[WARNING] Empty init_mask — skipping image.")
        return np.zeros_like(img_org, dtype=bool), img_org

    # Attempt up to max_attempts times with increasing avg_thresh
    attempt = 0

    while attempt < max_attempts:
        final_mask, final_contours, outer = process_mask(
            img_org,
            img,
            avg_thresh,
            min_contour_area,
            seed_thresh,
            median,
            erode_ksize,
            convex_hull
        )

        if np.count_nonzero(final_mask) > 0:
            # Success
            if save_plot:
                plot = plot_segmentation_result(img_org, outer, final_contours)
            else:
                plot = None

            return (polygon2mask(img_org.shape[:2], outer) if keep_init_mask else final_mask) > 0, plot

        else:
            attempt += 1
            avg_thresh += increase_avg
            print(f"[INFO] Final mask empty — increasing avg_thresh to {avg_thresh} (attempt {attempt}/{max_attempts})")

    print("[WARNING] All attempts failed — returning initial mask.")
    outer_contour_first = max(measure.find_contours(init_mask, 0.5), key=len)
    init_mask_poly = polygon2mask(img_org.shape[:2], outer_contour_first)
    eroded_init_mask = erode_mask(init_mask_poly, kernel_size=erode_ksize)
    outer_contour = max(measure.find_contours(eroded_init_mask, 0.5), key=len)

    final_mask = eroded_init_mask
    final_contours = [outer_contour]

    if save_plot:
        plot = plot_segmentation_result(img_org, outer_contour, final_contours)
    else:
        plot = None

    return final_mask > 0, plot
