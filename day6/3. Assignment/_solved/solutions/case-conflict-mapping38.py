protected_areas_border['geometry'] = protected_areas_border.buffer(10000).difference(protected_areas_utm.unary_union)